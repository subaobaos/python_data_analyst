#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-09-17 14:07
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : aes.py
# @Software: PyCharm

#                                                    __----~~~~~~~~~~~------___
#                                   .  .   ~~//====......          __--~ ~~
#                   -.            \_|//     |||\\  ~~~~~~::::... /~
#                ___-==_       _-~o~  \/    |||  \\            _/~~-
#        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
#    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
#  .~       .~       |   \\ -_    /  /-   /   ||      \   /
# /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
# |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
#          '         ~-|      /|    |-~\~~       __--~~
#                      |-~~-_/ |    |   ~\_   _-~            /\
#                           /  \     \__   \/~                \__
#                       _--~ _/ | .-~~____--~-/                  ~~==.
#                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
#                                 -_     ~\      ~~---l__i__i__i--~~_/
#                                 _-~-__   ~)  \--______________--~~
#                               //.-~~~-~_--~- |-------~~~~~~~~
#                                      //.-~~~--\
#               神兽保佑
#                  永无BUG!

import base64
from src.config import config
from Crypto.Cipher import AES


class Aestion():

    def __init__(self):

        self.key = config.SECRET_KEY
        self.aes = AES.new(
            str.encode(
                self.key),
            AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式

    # 补足字符串长度为16的倍数
    def add_to_16(self, s):
        while len(s) % 16 != 0:
            s += '\0'
        return str.encode(s)  # 返回bytes

    # 加密
    def encode_data(self, data):
        encrypted_text = str(
            base64.encodebytes(
                self.aes.encrypt(
                    self.add_to_16(data))),
            encoding='utf8').replace(
                '\n',
            '')
        return encrypted_text

    # 解密
    def decode_data(self, data):
        decrypted_text = str(
            self.aes.decrypt(
                base64.decodebytes(
                    bytes(
                        data,
                        encoding='utf8'))).rstrip(b'\0').decode("utf8"))
        return decrypted_text
