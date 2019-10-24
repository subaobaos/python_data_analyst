#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-24 23:16
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : panda_jsq.py
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
import re

class panda():

    def __init__(self, user, pwd):

        self.s = requests.session()
        self.user_name = user
        self.passwd = pwd
        self.expire_time = ''
        self.phone = ''
        self.pd_online = ''
        self.token = ''

    def pd_web_login(self):

        url = 'https://www.xiongmao789.com/api/ajax/ajax_check_user'

        data = {
            'username': self.user_name,
            'password': self.passwd,
            'check_code': '',
        }

        res = self.s.post(url, data=data)

        res = res.json()

        # print(res)
        # print(type(res))

        if res['success'] == 1:

            print(self.user_name + ' web登录成功')
            return 1

        else:

            print(res)
            return 0

    def get_dq_time(self):

        url = 'https://www.xiongmao789.com/Member/Center/'

        res = self.s.get(url)

        res = res.text

        re1 = r'<p>会员有效期至：<span>([\s\S]*?)</span></p>'
        reg1 = re.compile(re1)
        rece1 = reg1.findall(res)
        rece1 = rece1[0]

        print('会员到期时间:' + str(rece1))

    def pd_encode(self, number):
        if (number == '@'):
            return 'OF'

        elif (number == 'q'):
            return '3E'

        elif (number == 'w'):
            return '38'

        elif (number == 'e'):
            return '2A'

        elif (number == '.'):
            return '61'

        elif (number == 'c'):
            return '2C'

        elif (number == 'o'):
            return '20'

        elif (number == 'm'):
            return '22'

        elif (number == 'u'):
            return '3A'

        elif (number == 'a'):
            return 'aE'

        elif (number == 'j'):
            return '25'

        elif (number == 's'):
            return '3C'

        elif (number == 'b'):
            return '2D'

        elif (number == '1'):
            return '7E'

        elif (number == '2'):
            return '7D'

        elif (number == '3'):
            return '7C'

        elif (number == '4'):
            return '7B'

        elif (number == '5'):
            return '7A'

        elif (number == '6'):
            return '79'

        elif (number == '7'):
            return '78'

        elif (number == '8'):
            return '77'

        elif (number == '9'):
            return '76'

        elif (number == '0'):
            return '7F'

    def pd_pc_login(self):

        pd_encode_user = ''
        pd_encode_pwd = ''

        for i in self.user_name:
            pd_encode_user += self.pd_encode(i)

        for i in self.passwd:
            pd_encode_pwd += self.pd_encode(i)

        url = 'http://39.108.73.100/v1/user/login'

        data = {
            'username': pd_encode_user,
            'password': pd_encode_pwd,
            'mask': '2C2D787E7E292E2C29797B2A77792C7D7E767779787E7A777F7D792B772A7E2C',
            'appversion': '7B617E617E617F',
            'openid': '',
            'scope': '',
            'unionid': '',
            'client_ip': '223.167.32.194'}

        res = self.s.post(url, data=data)

        res = res.json()

        print(res)

        if res['code'] == 1:

            self.expire_time = res['data']['expire_time']
            self.phone = res['data']['phone']
            self.token = res['data']['token']

            print(self.user_name + ' pc登录成功 绑定手机：' + self.phone + '会员到期时间：' + self.expire_time)
            return 1

        else:
            print(self.user_name + ' pc登录失败')
            return 0


