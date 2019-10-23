#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 22:07
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : select_aes.py
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

import sys
from src.config import config
from src.utils import aes,mysqlhelper


T = True
while T == True:
    aes_instance = aes.Aestion()
    mysqlhelper_instance = mysqlhelper.Mysqlhelper()
    pd = input('请输入（0:加密 1:解密 2:插入）')
    if pd == '1':
        try:
            data = input('请输入需要解密的字符串：')
            print('解密成功！明文为：' + aes_instance.decode_data(data))
        except:
            print('解密失败！')
            sys.exit()
    elif pd == '2':
        account_name = input('站点名称：')
        account_user = aes_instance.encode_data(input('用户名称：'))
        account_pwd = aes_instance.encode_data(input('用户密码：'))
        resume = input('备注：')

        # SQL 插入语句  里面的数据类型要对应
        sql = "INSERT INTO account_info(account_name, \
               account_user, account_pwd, resume, creat_time) \
               VALUES ('%s', '%s',  '%s',  '%s', now())" % \
              (account_name, account_user, account_pwd, resume)

        mysqlhelper_instance.insert_data(sql)

    elif pd == '0':
        try:
            data = input('请输入需要加密的字符串：')
            print('加密成功！密文为：' + aes_instance.encode_data(data))
        except:
            print('加密失败！')
            sys.exit()

    else:
        print('您输入的指令不正确')
