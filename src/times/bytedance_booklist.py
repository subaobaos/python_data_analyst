#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-20 14:05
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : bytedance_booklist.py
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
from src.utils import mysqlhelper
import requests
import json
import pandas as pd

url = 'http://h-book.bytedance.net/api/book/list?offset=0&count=10000'
data = {
    'offset':'0',
    'count':'1000',
}

res = requests.get(url,data=data)
res = res.json()

j = 0
for i in res['bookList']:
    j += 1
    print(i)
    print('\n')

print('共'+str(j)+'条记录')

df = pd.DataFrame(res['bookList'])
print(df)

mysqlhelper_instance = mysqlhelper.Mysqlhelper(**config.mysql_aliyun)
mysqlhelper_instance.creat_table(df, '1220_byte_bookdata')
df.to_csv(r'D:\byte_data\yibo.csv',encoding="utf_8_sig")