#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-01-27 19:30
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : dama_lz.py
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
from src.config import config

title = '联众打码平台'

class liangZhong():

    def __init__(self,user=config.lz_user,pwd=config.lz_pwd):

        self.user = user
        self.pwd = pwd

    def lianzhong_login(self):
        url = 'https://v2-api.jsdama.com/check-points'

        data = {
            'softwareId': '13806',
            'softwareSecret': 'QZvItXgTd5mmR4Rp30JCXW7wUHOUkUFqTxKKLOxE',
            'username': self.user,
            'password': self.pwd
        }
        try:

            rece = requests.post(url, json=data)
            rece = rece.json()

            userPoints = rece['data']['userPoints']
            availablePoints = rece['data']['availablePoints']
            lockPoints = rece['data']['lockPoints']

            print(
                '登陆成功！用户剩余总点数:' +
                userPoints +
                ',⽤用户可⽤用点数:' +
                availablePoints +
                ',用户锁定点数:' +
                lockPoints)
        except BaseException:
            print('联众打码登陆失败\n')

    def lianzhong_shibie(self, image_url, type_id):

        image_url = image_url.encode()

        image = requests.get(image_url)
        ck_lianzhong = image.cookies.get_dict()
        # print(">>>ck_lianzhong:" + str(ck_lianzhong))

        image = image.content

        url = 'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload'

        data = {
            'user_name': self.user,
            'user_pw': self.pwd,
            'yzmtype_mark': type_id
        }
        files = {
            'upload': image
        }
        try:
            rece = requests.post(url, data=data, files=files)
            rece = rece.json()
            dtjg = rece['data']['val']
            print('联众识别成功！验证码：' + dtjg + '\n')
            return {'code': 1, 'dtjg': dtjg, 'ck': ck_lianzhong}
        except BaseException:
            print('联众识别失败！\n')
            return {'code': 0}

if __name__ == '__main__':

    lianzhong = liangZhong(config.lz_user,config.lz_pwd)

    url = 'https://www.htjsq.com/captcha.php?0.025871909668330195'

    lianzhong.lianzhong_shibie(url, '1001')
