#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-25 14:05
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : xun_proxy.py
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

from config import config
import requests
import json


class XunProxy():

    def __init__(self):
        self.spiderId = config.xun_proxy['spiderId']
        self.order_number = config.xun_proxy['order_number']

    def start(self):
        url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=" + self.spiderId + "&orderno=" + self.order_number + "&returnType=2&count=1"
        rece = requests.get(url)
        rece = rece.json()
        print(res)
        port = rece['RESULT'][0]['port']
        ip = rece['RESULT'][0]['ip']
        return ip, port


    def switch_proxy(self):
        pass
