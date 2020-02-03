#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-11-30 16:00
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : aqs_test.py
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
import hashlib
from src.config import config

data = config.aqs_api

def get_sign(arge,AppSecret):

    # 对所有API请求参数（包括公共参数和业务参数，但除去sign参数和byte[]
    # 类型的参数），根据参数名称的ASCII码表的顺序排序。如：foo = 1, bar = 2, foo_bar = 3, foobar = 4
    # 排序后的顺序是bar = 2, foo = 1, foo_bar = 3, foobar = 4。
    # 将排序好的参数名和参数值拼装在一起，根据上面的示例得到的结果为：bar2foo1foo_bar3foobar4。
    # 把拼装好的字符串采用utf - 8
    # 编码，在拼装的字符串前后加上app的secret后，使用MD5算法进行摘要，如：md5(secret + bar2foo1foo_bar3foobar4 + secret)

    arge = sorted(arge)
    x = AppSecret + arge[0] + arge[1] + AppSecret
    print(x)
    md5_arge = get_md5(x)
    print(md5_arge)
    return md5_arge

def get_md5(x):
    m = hashlib.md5()
    m.update(x.encode("utf-8"))
    print(m)
    x = m.hexdigest()
    return x
t = int(time.time())
AppId = data['AppId']
AppSecret = data['AppSecret']
token = data['token']

headers = {}
headers['Authorization'] = 'Bearer ' + token
headers['ApiVersion'] = '1'

# api业务参数
params = []
params.append('timestamp' + str(t))
params.append('tid' + '835103587684501751')

data = {}
data['sign'] = get_sign(params,AppSecret)
data['timestamp'] = t
data['tid'] = 835103587684501751
print(data)

url = 'http://gw.api.agiso.com/alds/Trade/TradeInfo'

res = requests.post(url=url,data=data,headers=headers)
res = res.json()
print(res)
