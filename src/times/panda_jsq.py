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
import time
import requests
import re
import datetime

class panda():

    def __init__(self, user, pwd):

        self.s = requests.session()
        self.user_name = user
        self.passwd = pwd
        self.pd_encode_user = ''
        self.pd_encode_pwd = ''
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

        for i in self.user_name:
            self.pd_encode_user += self.pd_encode(i)

        for i in self.passwd:
            self.pd_encode_pwd += self.pd_encode(i)

        url = 'http://39.108.73.100/v1/user/login'

        data = {
            'username': self.pd_encode_user,
            'password': self.pd_encode_pwd,
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


    def pd_check(self):

        url = 'http://39.108.73.100/v1/user/deprecate'

        data = {
            'username': self.pd_encode_user,
            'password': self.pd_encode_pwd,
            'client_version': '7B617F617A617F',
            'client_ip': '7D7D7C617E7979617C7D617C',
            'platform': '7B',
            'mask': '7B2A7A2E792D772E7A2978787D2D797A7E2B2B2B2E2A7C292D2E7E767A2D7B2A',
            'channel': '3C3B2E212B2E3D2B',
            'client_id': 'ac12247a07ef0001fcb7'}

        rece = requests.post(url, data=data)

        rece = rece.json()

        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在

        # {'code': 1, 'msg': 'no connection', 'data': {'online': 0, 'expire': 0}}

        if (rece['code'] == 1):
            time.sleep(2)
            is_online = nowTime + '暂时无人加速'
            # url = 'http://api.xiongmao555.com/v1/game/free-list'
            # data = {
            #     'token': self.token,
            #     'client_version': '7B617F617A617F',
            #     'client_ip': '7D7D7C617E7979617C7D617C',
            #     'platform': '7B',
            #     'mask': '7B2A7A2E792D772E7A2978787D2D797A7E2B2B2B2E2A7C292D2E7E767A2D7B2A',
            #     'channel': '3C3B2E212B2E3D2B',
            # }

            url = 'http://39.108.73.100/v1/report/submit-fault'
            data = {
                'username': self.pd_encode_user,
                'password': self.pd_encode_pwd,
                'client_id': 'ac12247a07ef0001fcb7',
                'token': self.token,
                'client_version': '7B617F617A617F',
                'client_ip': '7D7D7C617E7979617C7D617C',
                'platform': '7B',
                'mask': '7B2A7A2E792D772E7A2978787D2D797A7E2B2B2B2E2A7C292D2E7E767A2D7B2A',
                'channel': '3C3B2E212B2E3D2B',
                'connect_length': '36531',
                'connect_id': '8258',
                'proxy_mode': '\u6a21\u5f0f\u4e00',
                'game_id': '8104',
                'provider': '352',
                'state': '1',
                'connect_ip': '223.167.32.194',
            }

            rece = requests.post(url, data=data)

            rece = rece.json()
            # print(rece)

        else:
            is_online = nowTime + '正在加速中'

        return is_online


if __name__ == '__main__':

    a = panda('15665426103@qq.com','jsb122085')

    a.pd_pc_login()

    rece2 = a.pd_check()
    print(rece2)
