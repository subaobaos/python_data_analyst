#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-01-12 01:07
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : key_create.py
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


from src.utils import aes,mysqlhelper
import random

class Key():

    def __init__(self):
        aes_instance = aes.Aestion()
        self.mysqlhelper_instance = mysqlhelper.Mysqlhelper()
        self.km_mysql = mysqlhelper.Mysqlhelper(db='km')


    def create_key(self,number,leixin,resume,tablename='gq_xm_jhm',is_gzh=False):

        print(tablename)

        if tablename == 'gq_xm_jhm':

            key_leixin = int(leixin)
            key_resume = str(resume)
            keylist = ''
            key_list = ''

            while(number > 0):

                key = str(random.randint(0,99999999)).zfill(13)
                key_list = key_list + key + '\n'
                geshi  = 'a:1:{s:3:"key";s:13:"' + key + '";}'

                if number - 1 <= 0:
                    keylist = keylist + "'" + key
                else:
                    keylist = keylist + "'" + key + "',"

                sql = "INSERT INTO gq_xm_jhm(jihuoma, \
                       `type`, leixin, resume, jr_time) \
                       VALUES ('%s', '1', '%s',  '%s', now())" % \
                      (key, key_leixin, key_resume)

                self.mysqlhelper_instance.insert_data(sql)
                if is_gzh == True:
                    sql2 = "insert into ims_ewei_shop_virtual_data (uniacid,typeid,pvalue,fields,createtime) value ('3','5','%s','%s','1581136292')" % (key,geshi)

                    self.km_mysql.insert_data(sql2)

                number -= 1

        elif tablename == 'gq_htkey_table':

            key_leixin = int(leixin)
            key_resume = str(resume)
            keylist = ''
            key_list= ''

            while (number > 0):
                key = str(random.randint(0, 99999999)).zfill(13)
                key_list = key_list + key + '\n'

                if number - 1 <= 0:
                    keylist = keylist + "'" + key
                else:
                    keylist = keylist + "'" + key + "',"

                sql = "INSERT INTO gq_htkey_table(key_number, \
                       key_status, key_type, key_resume, key_maketime) \
                       VALUES ('%s', '1', '%s',  '%s', now())" % \
                      (key, key_leixin, key_resume)

                self.mysqlhelper_instance.insert_data(sql)

                number -= 1
        else:

            pass

        print(key_list)
        return keylist


if __name__ == '__main__':

    new_key = Key()

    new_key.create_key(100,'2','公众号',is_gzh=True)


