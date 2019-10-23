#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-09-30 00:24
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : mydbpools.py
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
from DBUtils.PooledDB import PooledDB
from src.config import config
import time

'''
@功能:PT数据库连接池
'''


class DBonnectionPools(object):
    __pool = None

    def __init__(self, ):
        pass

    def __enter__(self):
        self.conn = self.__getConn()
        self.cursor = self.conn.cursor()
        print("PT数据库创建con和cursor")
        return self

    def __getConn(self, host, port, user, pwd, db, charset):
        if self.__pool is None:
            start = time.time()

            self.__pool = PooledDB(creator=pymysql, mincached=config.DB_MIN_CACHED, maxcached=config.DB_MAX_CACHED,
                                   maxshared=config.DB_MAX_SHARED, maxconnections=config.DB_MAX_CONNECYIONS,
                                   blocking=config.DB_BLOCKING, maxusage=config.DB_MAX_USAGE,
                                   setsession=config.DB_SET_SESSION,
                                   host=host, port=port, user=user, passwd=pwd, db=db, use_unicode=True,
                                   charset=charset)

            end = time.time()

        return self.__pool.connection()

    """
    @summary: 释放连接池资源
    """

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

        print("PT连接池释放con和cursor")

    """
    重连接池中取出一个连接
    """

    def getconn(self, host, port, user, pwd, db, charset):
        conn = self.__getConn(host, port, user, pwd, db, charset)
        # cursor = conn.cursor()
        return conn


'''
# @功能:获取PT数据库连接
'''


def getDBonnectionPools():
    return DBonnectionPools()
