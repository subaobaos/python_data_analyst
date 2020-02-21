#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-02-21 19:42
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : cat_api.py
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

import re
import pymysql
from src.config import config

class Catapi():

    def __init__(self,mysql_user=config.mysqluser,mysql_password=config.mysqlpwd):

        self.db = pymysql.connect(
            host="47.99.90.3",
            user=mysql_user,
            password=mysql_password,
            db="database1",
            charset="utf8")
        self.cur = self.db.cursor()

    def get_code(self,phone):

        sql1 = '''
        SELECT smsContent FROM sms_recv WHERE PhoNum = {0} and smsDate between date_add(now(), interval - 5 minute) and now()
        '''.format(phone)
        self.cur.execute(sql1)
        code = self.cur.fetchall()

        if not code:
            print('暂无验证码')
            self.cur.close()
            self.db.close()
            return 0

        else:

            cod_econtent = code[0][0]
            print(cod_econtent)

            re1 = r'[0,1,2,3,4,5,6,7,8,9]{6}'
            reg = re.compile(re1)
            res = reg.findall(cod_econtent)
            res = res[0]
            print(res)
            self.cur.close()
            self.db.close()
            return res


if __name__ == '__main__':

    a = Catapi()

    a.get_code('16731021297')
