#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-31 10:39
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : panda_pwd_amend.py
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

from src.config import config
from src.utils import aes
import requests
import time
import re
import datetime
import pymysql
import sys
import json

def get_tbody(rece):
    try:
        re1 = r'<tbody>([\s\S]*?)</tbody>'
        reg1 = re.compile(re1)
        rece1 = reg1.findall(rece)
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

        print('a:' + str(a) + '-----------b:' + str(b))

        if (a > b):
            re4 = r'【熊猫加速器】验证码([\s\S]*?)，您正在注册'
            reg4 = re.compile(re4)
            rece4 = reg4.findall(rece2)
            rece4 = rece4[0]
            return rece4
        else:
            return 0

    except BaseException:
        return 0


encryption_instance = aes.Aestion()
xh_token = encryption_instance.decode_data(config.xh_token)

DB = config.mysql_aliyun
host = DB["host"]
port = DB["port"]
user = DB["user"]
pwd = DB["pwd"]
db = DB["db"]

url = 'https://subaobao.club/xhpt/tokenyz.php'

data = {
    'token': xh_token
}

rec = requests.post(url, data=data)

rec = json.loads(rec.text)

if rec['code'] == '1':
    xh_user = rec['xh_user']
    xh_password = rec['xh_pwd']

else:
    print('数据出现错误')
    sys.exit()

j = 1
while(j > 0):
    db = pymysql.connect(
        host=encryption_instance.decode_data(host),
        port=int(encryption_instance.decode_data(port)),
        user=encryption_instance.decode_data(user),
        password=encryption_instance.decode_data(pwd),
        db=encryption_instance.decode_data(db),
        charset="utf8")
    cur = db.cursor()

    sql = """select xm_zh,xm_bd_phone from gq_xm_table where xm_type='0' and xm_dq_time < now() and id not in (48)  and xm_type <> '过期' and xm_type <> '冻结' """
    cur.execute(sql)
    xiongmao = cur.fetchall()

    for line in xiongmao:
        xm_hao = line[0]
        xm_phone = line[1]
        print(xm_hao, xm_phone)

        # 发送验证码

        url = 'https://www.xiongmao789.com/api/ajax/Sendfindpasscode'

        data = {
            'username': xm_phone,
            'check_code': ''
        }

        headers = {
            'origin': 'https://www.xiongmao789.com',
            'referer': 'https://www.xiongmao789.com/findpwd/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3766.2 Safari/537.36'
        }

        rece = requests.post(url, data=data, headers=headers)
        xmck = rece.cookies.get_dict()
        rece = rece.text
        print(rece)

        b = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        b = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S")

        # 获取验证码
        t = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        url = 'http://47.110.86.5:9999/index.php?g=cust&m=login&a=dologin'

        data = {
            'username': xh_user,
            'password': xh_password
        }
        headers = {
            'Host': '47.110.86.5:9999',
            'Origin': 'http://47.110.86.5:9999',
            'Referer': 'http://47.110.86.5:9999/index.php?g=cust&m=login&a=index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        rece = requests.post(url, data=data, headers=headers)
        cookies = rece.cookies.get_dict()

        i = 0
        while (i < 10):
            url = 'http://47.110.86.5:9999/index.php?g=cust&m=smscust&a=receive'

            data = {
                'msgid': '',
                'mobile': xm_phone,
                'content': '',
                'startDate': t,
                'endDate': t
            }

            rece = requests.post(
                url,
                data=data,
                headers=headers,
                cookies=cookies)
            rece = rece.text

            dxnr = get_tbody(rece)
            if (dxnr != 0):
                print(dxnr)
                break
            else:
                i += 1
                time.sleep(5)

        # 提交修改密码

        new_pwd = 'jsb' + dxnr
        print(new_pwd)

        url = "https://www.xiongmao789.com/Member/Password/findpass_check"
        data = {
            'username': xm_phone,
            'code': dxnr
        }
        headers = {
            'origin': 'https://www.xiongmao789.com',
            'referer': 'https://www.xiongmao789.com/findpwd/',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        rece = requests.post(url, data=data, headers=headers, cookies=xmck)
        rece = rece.json()
        print(rece)

        url = "https://www.xiongmao789.com/Member/Password/step3"

        data = {
            'username': xm_hao,
            'phone': xm_phone,
            'code': dxnr,
            'password1': new_pwd,
            'password2': new_pwd
        }

        rece = requests.post(url, data=data, headers=headers, cookies=xmck)
        print(rece)

        # 更新熊猫表
        sql = """update gq_xm_table set xm_mm = '%s',xm_type='1' where xm_bd_phone = '%s'""" % (
            new_pwd, xm_phone)
        cur.execute(sql)
        db.commit()
        time.sleep(2)

    db.close()
    print('循环结束')

    time.sleep(500)

