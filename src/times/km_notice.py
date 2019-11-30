#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-11-30 15:03
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : km_notice.py
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
from src.utils import aes,robot
import time
import datetime
import pymysql

while True:
    encryption_instance = aes.Aestion()

    DB = config.km_bidata
    host = DB["host"]
    port = DB["port"]
    user = DB["user"]
    pwd = DB["pwd"]
    db = DB["db"]


    db = pymysql.connect(
        host=encryption_instance.decode_data(host),
        port=int(encryption_instance.decode_data(port)),
        user=encryption_instance.decode_data(user),
        password=encryption_instance.decode_data(pwd),
        db=encryption_instance.decode_data(db),
        charset="utf8")
    cur = db.cursor()

    sql = '''
    SELECT
            unix_timestamp(now()),
            carrier as '用户信息',
            createtime as '创建时间',
            finishtime,
            paytime as '支付时间',
            sendtime as '提交时间',
            virtual_str as '购买商品',
            virtual_info as '发货信息',
            goodsprice as '支付金额'
    FROM
            ims_ewei_shop_order
    ORDER BY
            id DESC
    LIMIT
            1
    '''

    cur.execute(sql)

    od = cur.fetchall()

    timestamp = od[0][4]
    shopname = od[0][6]

    time_local = time.localtime(timestamp)

    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

    dt = datetime.datetime.strptime(
        dt, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=5)

    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowtime = datetime.datetime.strptime(nowtime, "%Y-%m-%d %H:%M:%S")


    if dt >= nowtime:
        str = '新订单!' +' 购买商品：'+str(shopname)
        robot.dingding_robot(str)
    else:
        pass
    print('循环结束')
    time.sleep(300)
    db.close()
