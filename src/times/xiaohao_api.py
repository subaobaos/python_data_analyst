#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 21:57
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : xiaohao_api.py
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
import json
import sys
import datetime
import time
import re
from src.config import config
from src.utils import aes

encryption_instance = aes.Aestion()

xh_token = encryption_instance.decode_data(config.xh_token)

class xhpt():

    def __init__(self, user, pwd):
        self.xh_user = user
        self.xh_password = pwd
        self.b = datetime.datetime.strptime(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "%Y-%m-%d %H:%M:%S")
        self.s = requests.session()
        self.rece_body = ''
        self.t = ''

    def get_login(self):
        self.t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        url = 'http://103.99.210.71:1111'

        rece = self.s.get(url)
        rece = rece.text

        re1 = r"name='_tn' value='([\s\S]*?)'/> <input name"
        reg1 = re.compile(re1)
        rece1 = reg1.findall(rece)
        tn = rece1[0]
        print(tn)

        url = 'http://103.99.210.71:1111/index.php?g=cust&m=login&a=dologin'
        data = {
            '_tn': tn,
            'username': self.xh_user,
            'password': self.xh_password
        }
        headers = {
            "Host": "103.99.210.71:1111",
            "Connection": "keep-alive",
            "Content-Length": "86",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept": "*/*",
            "Origin": "http://103.99.210.71:1111",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://103.99.210.71:1111/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        res = self.s.post(url, data=data, headers=headers)
        return res

    def get_yzmbody(self):
        url = 'http://103.99.210.71:1111/index.php?g=cust&m=smscust&a=receive'

        data = {
            'msgid': '',
            'mobile': phone_number,
            'content': '',
            'startDate': self.t,
            'endDate': self.t
        }

        headers = {
            "Host": "103.99.210.71:1111",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        rece = self.s.post(url, data=data, headers=headers)
        self.rece_body = rece.text

    def get_yzm(self):
        try:
            re1 = r'<tbody>([\s\S]*?)</tbody>'
            reg1 = re.compile(re1)
            rece1 = reg1.findall(self.rece_body)
            rece1 = rece1[0]

            re2 = r'<tr>([\s\S]*?)</tr>'
            reg2 = re.compile(re2)
            rece2 = reg2.findall(rece1)
            rece2 = rece2[0]  # 最新的一条tr


            re3 = r'<td width="110">([\s\S]*?)</td>'
            reg3 = re.compile(re3)
            rece3 = reg3.findall(rece2)
            rece3 = rece3[0]  # 时间
            #print(rece3)

            # a = datetime.datetime.strptime(
            #     rece3, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=1)
            #
            # print('a:' + str(a) + '-----------b:' + str(self.b))

            re4 = r'td width="60">([\s\S]*?)</td> <td  width="160">'
            reg4 = re.compile(re4)
            rece4 = reg4.findall(rece2)
            rece_phone = rece4[0]

            #print(rece_phone)

            re5 = r'width="160">([\s\S]*?)From'
            reg5 = re.compile(re5)
            rece5 = reg5.findall(rece2)
            rece_content = rece5[0]

            #print(rece_content)

            return rece3,rece_phone,rece_content

            # if (a > self.b):
            #     re4 = r'【雷神】您的验证码：([\s\S]*?)，有效时间30分钟'
            #     reg4 = re.compile(re4)
            #     rece4 = reg4.findall(rece2)
            #     rece4 = rece4[0]
            #     return str(rece2),str(rece4)
            # else:
            #     return 0

        except BaseException:
            return 0

    def get_notice(self):

        url = 'http://103.99.210.71:1111/index.php?g=cust&m=center&a=cust_home'

        headers = {
            "Host": "103.99.210.71:1111",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        res = self.s.get(url,headers=headers)

        print(res.text)


url = 'https://subaobao.club/xhpt/tokenyz.php'

data = {
    'token': xh_token
}

rec = requests.post(url, data=data)

rec = json.loads(rec.text)

if rec['code'] == '1':
    xh_user = rec['xh_user']

    xh_pwd = rec['xh_pwd']

    mysql_user = rec['sql_user']

    mysql_password = rec['sql_pwd']

else:
    print('数据出现错误')
    sys.exit()

xh = xhpt(xh_user, xh_pwd)

xh.get_login()

T = True

while(T):

    phone_number = input('请输入手机号：\n')

    xh.get_yzmbody()

    c1, c2, c3 = xh.get_yzm()

    print(f'时间：{c1}\n')
    print(f'手机号：{c2}\n')
    print(f'验证码：{c3}\n')

    is_chaxun = input('是否继续查询：(是/否)：\n')

    if is_chaxun != '是':

        print('程序已退出\n')
        sys.exit()




