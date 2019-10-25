#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 12:01
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : leisheng_check.py
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
from src.times import leisheng_jsq
import pymysql
import time
import datetime

encryption_instance = aes.Aestion()

DB = config.mysql_aliyun
host = DB["host"]
port = DB["port"]
user = DB["user"]
pwd = DB["pwd"]
db = DB["db"]


nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在

db = pymysql.connect(
    host=encryption_instance.decode_data(host),
    port=int(encryption_instance.decode_data(port)),
    user=encryption_instance.decode_data(user),
    password=encryption_instance.decode_data(pwd),
    db=encryption_instance.decode_data(db),
    charset="utf8")
cur = db.cursor()

sql = """select ls_hao,ls_mm from ls_51_huodong where id not in (1,2)  """
cur.execute(sql)
leisheng = cur.fetchall()


for line in leisheng:

    ls_hao = line[0]
    ls_mm = line[1]

    print(ls_hao,ls_mm)

    ls = leisheng_jsq.LeiSheng(ls_hao,ls_mm,ls_mm)

    ls.ls_stop()

    print('登录成功 剩余时间：'+ str(ls.ls_sytime))

    ############ 将数据更新到雷神表 #################

    sql = """update ls_51_huodong set sy_time = '%s' where ls_hao = '%s'""" % (
        ls.ls_sytime, ls_hao)
    cur.execute(sql)
    db.commit()
    time.sleep(5)

db.close()
