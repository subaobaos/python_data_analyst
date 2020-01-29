#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-01-27 16:26
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : banma.py
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

title = '斑马平台api'

class Banma():

    def __init__(self,user,pwd,sid):

        self.url = 'http://api.banma1024.net/api/do.php'
        self.user = user
        self.pwd = pwd
        self.token = ''
        self.sid = sid
        self.message = ''

    def loginIn(self):

        url = self.url
        data = {
            'action': 'loginIn',
            'name': self.user,
            'password': self.pwd
        }
        res = requests.post(url,data=data)
        res = res.text

        status = res[:1]
        self.token = res[2:]

        if status == '1':
            print('status:' + str(status) + ' token:' + str(self.token))
            return self.token

        else:
            print('res:' + res)
            return '失败'

    def getSummary(self):

        url = self.url
        data = {
            'action': 'getSummary',
            'token': self.token
        }
        res = requests.post(url,data=data)
        res = res.text
        print(res+'\n')

    def getPhone(self):

        url = self.url
        data = {
            'action': 'loginIn',
            'sid': self.sid,
            'token': self.token,
            'author':'subaobaos'
        }
        res = requests.post(url,data=data)
        res = res.text

        status = res[:1]
        self.phone = res[2:]

        if status == '1':
            print('status:' + str(status) + ' 手机号:' + str(self.phone))
            return self.phone

        else:
            print('res:' + res)
            return '失败'

    def getMessage(self):

        url = self.url
        data = {
            'action': 'getMessage',
            'sid': self.sid,
            'phone': self.phone,
            'token': self.token,
            'author':'subaobaos'
        }
        res = requests.post(url,data=data)
        res = res.text

        status = res[:1]
        self.message = res[2:]

        if status == '1':
            print('status:' + str(status) + ' 验证码:' + str(self.message))
            return self.message

        else:
            print('res:' + res)
            return '失败'

    def addBlacklist(self):

        url = self.url
        data = {
            'action': 'addBlacklist',
            'sid': self.sid,
            'phone': self.phone,
            'token': self.token
        }
        res = requests.post(url,data=data)
        res = res.text

        status = res[:1]

        if status == '1':
            print('status:' + str(status) + ' 加黑结果:' + str(self.message))
            return '成功'

        else:
            print('res:' + res)
            return '失败'


if __name__ == '__main__':

    banma = Banma(config.apiuser,config.apipwd)

    banma.loginIn()

    banma.getSummary()
