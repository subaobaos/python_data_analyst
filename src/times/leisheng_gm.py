#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-01-10 22:47
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : leisheng_gm.py
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

import pymysql
import re
import requests
import time
import hashlib
import datetime
import json
import sys


class LeiSheng():

    def __init__(self, user, pwd):

        self.ls_hao = user
        self.ls_mm = pwd
        self.ls_md5_mm = ''
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


class xhpt():

    def __init__(self, user, pwd):
        self.xh_user = user
        self.xh_password = pwd
        self.s = requests.session()
        self.b = datetime.datetime.strptime(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "%Y-%m-%d %H:%M:%S")
        self.tn = ''
        self.rece_body = ''
        self.t = ''

    def get_login(self):
        self.t = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        url = 'http://121.40.17.58:9999'

        rece = self.s.get(url)
        rece = rece.text

        re1 = r"name='_tn' value='([\s\S]*?)'/> <input name"
        reg1 = re.compile(re1)
        rece1 = reg1.findall(rece)
        self.tn = rece1[0]


        url = 'http://121.40.17.58:9999/index.php?g=cust&m=login&a=dologin'
        data = {
            '_tn': self.tn,
            'username': self.xh_user,
            'password': self.xh_password
        }
        headers = {
            "Host": "121.40.17.58:9999",
            "Connection": "keep-alive",
            "Content-Length": "86",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept": "*/*",
            "Origin": "http://121.40.17.58:9999",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://121.40.17.58:9999/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        rece = self.s.post(url, data=data, headers=headers)
        return rece.text


    def get_yzmbody(self):
        url = 'http://121.40.17.58:9999/index.php?g=cust&m=smscust&a=receive'

        data = {
            'msgid': '',
            'mobile': ls.ls_hao,
            'content': '',
            '_tn:': self.tn,
            'startDate': self.t,
            'endDate': self.t
        }

        headers = {
            'Host': '121.40.17.58:9999',
            'Origin': 'http://121.40.17.58:9999',
            'Referer': 'http://121.40.17.58:9999/index.php?g=cust&m=login&a=index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
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

            a = datetime.datetime.strptime(
                rece3, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=1)

            print('a:' + str(a) + '-----------b:' + str(self.b))

            if (a > self.b):
                re4 = r'【雷神】您的验证码：([\s\S]*?)，有效时间30分钟'
                reg4 = re.compile(re4)
                rece4 = reg4.findall(rece2)
                rece4 = rece4[0]
                return rece4
            else:
                return 0

        except BaseException:
            return 0


url = 'https://subaobao.club/xhpt/tokenyz.php'

data = {
    'token': ''
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

j = 1

while(j > 0):
    db = pymysql.connect(
        host="47.99.90.3",
        user=mysql_user,
        password=mysql_password,
        db="database1",
        charset="utf8")
    cur = db.cursor()

    sql = """select ls_hao,ls_mm from qh_ls_table where ls_status='0' and ls_expiretime < now()"""
    cur.execute(sql)
    leisheng = cur.fetchall()

    xh = xhpt(xh_user, xh_pwd)

    for line in leisheng:

        ls = LeiSheng(line[0], line[1])
        print(ls.__dict__)

        ls.get_md5()

        ls.ls_stop()

        ls.ls_pull_yzm()

        xh.get_login()

        i = 0
        while (i < 15):

            xh.get_yzmbody()

            dxnr = xh.get_yzm()

            if (dxnr != 0):
                print(dxnr)
                break
            else:
                i += 1
                time.sleep(5)

        if (dxnr == 0):
            print('暂时无法收取验证码 已跳过')
            continue

        ls.ls_push_yzm(dxnr=dxnr)

        print(ls.__dict__)

        # 更新雷神表
        sql = """update qh_ls_table set ls_mm = '%s',ls_status='1',ls_viptime='%s' where ls_hao = '%s'""" % (
            ls.ls_mm, ls.ls_sytime, ls.ls_hao)
        cur.execute(sql)
        db.commit()
        time.sleep(3)

    db.close()

    time.sleep(300)
