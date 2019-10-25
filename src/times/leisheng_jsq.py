#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 10:40
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : leisheng_jsq.py
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

import requests
import hashlib


class LeiSheng():

    def __init__(self, user, pwd, md5_pwd):

        self.ls_hao = user
        self.ls_mm = pwd
        self.ls_md5_mm = md5_pwd
        self.ls_token = ''
        self.ls_sytime = ''
        self.verify_key = ''

    def get_md5(self):
        m = hashlib.md5()
        m.update(self.ls_mm.encode("utf8"))
        self.ls_md5_mm = m.hexdigest()

    def ls_stop(self):
        url = 'https://webapi.leigod.com/wap/login/bind'
        data = {
            'code': '',
            'country_code': 86,
            'lang': 'zh_CN',
            'password': self.ls_md5_mm,
            'src_channel': 'guanwang',
            'user_type': '0',
            'username': self.ls_hao
        }
        headers = {
            'origin': 'https://m.leigod.com',
            'referer': 'https://m.leigod.com/mlogin.html?platform=4&code=GdHKVOoMXqghXM9x&state_html=mcenterList',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        rece = requests.post(url=url, data=data, headers=headers)
        rece = rece.json()
        print(rece)
        self.ls_token = rece['data']['login_info']['account_token']

        url = 'https://webapi.leigod.com/api/user/pause'
        data = {
            'account_token': self.ls_token,
            'lang': 'zh_CN'
        }
        headers = {
            'origin': 'https://m.leigod.com',
            'referer': 'https://m.leigod.com/mpause.html?region_code=1&language=zh_CN&platform=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

        rece = requests.post(url=url, data=data, headers=headers)
        rece = rece.json()

        url = 'https://webapi.leigod.com/api/user/info'

        data = {
            'account_token': self.ls_token,
            'lang': 'zh_CN'
        }

        rece = requests.post(url=url, data=data, headers=headers)
        rece = rece.json()

        self.ls_sytime = rece['data']['expiry_time']

    def ls_pull_yzm(self):
        url = 'https://webapi.leigod.com/api/user/verify_code'

        data = {
            'account_token': self.ls_token,
            'lang': 'zh_CN'
        }

        headers = {
            'origin': 'https://user.leigod.com',
            'referer': 'https://user.leigod.com/login.html?region_code=1&language=zh_CN',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

        rece = requests.post(url, data=data, headers=headers)
        rece = rece.json()
        print(rece)
        self.verify_key = rece['data']['verify_key']
        print(self.verify_key)

    def ls_push_yzm(self, dxnr):
        self.ls_mm = 'jsb' + dxnr

        self.get_md5()

        url = 'https://webapi.leigod.com/api/user/password_code'
        data = {
            'account_token': self.ls_token,
            'lang': 'zh_CN',
            'new_password': self.ls_md5_mm,
            'new_password_confirmation': self.ls_md5_mm,
            'verify_code': dxnr,
            'verify_key': self.verify_key
        }
        headers = {
            'origin': 'https://user.leigod.com',
            'referer': 'https://user.leigod.com/login.html?region_code=1&language=zh_CN',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

        rece = requests.post(url, data=data, headers=headers)
        print(rece.text)
