#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 00:15
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : panda_check.py
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
from src.times import panda_jsq
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

sql = """select xm_zh,xm_mm from gq_xm_table where xm_type not in ('冻结','过期')  """
cur.execute(sql)
xiongmao = cur.fetchall()

for line in xiongmao:

    xm_hao = line[0]
    xm_mm = line[1]

    print(xm_hao)
    print(xm_mm)

    a = panda_jsq.panda(xm_hao,xm_mm)

    if a.pd_pc_login() == 1:

        isonline = a.pd_check()

        ############ 将数据更新到熊猫表 #################

        sql = """update gq_xm_table set xm_jr_time = '%s',xm_yzm = '%s' where xm_zh = '%s'""" % (
            a.expire_time,isonline, xm_hao)
        cur.execute(sql)
        db.commit()
        time.sleep(5)

db.close()
