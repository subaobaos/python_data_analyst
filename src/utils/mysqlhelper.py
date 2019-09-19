#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-09-17 18:17
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : mysqlhelper.py
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
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import re

DB = config.mysql_aliyun
host = DB["host"]
port = DB["port"]
user = DB["user"]
pwd = DB["pwd"]
db = DB["db"]

encryption_instance = aes.Aestion()


class Mysqlhelper():

    def __init__(
            self,
            host=host,
            port=port,
            user=user,
            pwd=pwd,
            db=db,
            charset='utf8',):

        self.host = encryption_instance.decode_data(host)
        self.port = int(encryption_instance.decode_data(port))
        self.user = encryption_instance.decode_data(user)
        self.pwd = encryption_instance.decode_data(pwd)
        self.db = encryption_instance.decode_data(db)
        self.charset = charset

    def get_conn(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.pwd,
                db=self.db,
                charset=self.charset,
            )
            print('\n数据库连接成功')

        except BaseException:
            print('\n数据库连接失败')

        return conn

    def get_df(self, sql):

        try:

            sql = self.sql_clean(sql)

            self.conn = self.get_conn()

            df = pd.read_sql(sql, self.conn)

            print('get_df成功 shape:{0}'.format(df.shape))

            self.close(self.conn)

        except BaseException:

            print('get_df失败')

        return df

    def creat_table(self, df, table):

        a = 'mysql+pymysql://' + self.user + ':' + self.pwd + \
            '@' + self.host + ':' + str(self.port) + '/' + self.db

        try:
            engine = create_engine(
                a,
                encoding='utf8')

            df.to_sql(table, engine, if_exists='replace', index=False)

            print('创建表' + str(table) + '成功！')
        except BaseException:

            print('创建表' + str(table) + '失败！')

    def insert_data(self, sql):

        sql = self.sql_clean(sql)

        self.conn = self.get_conn()

        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()

        try:
            cursor.execute(sql)
            self.conn.commit()
            print('数据插入成功！')
        except BaseException:
            # 发生错误时回滚
            self.conn.rollback()
            print('数据插入失败！')
        # 关闭数据库连接
        self.close(self.conn, cursor)

    def sql_clean(self, sql):

        sql = re.sub(r"\,\s*\)", ")", sql)

        return sql

    def close(self, conn, cursor=None):

        try:
            if cursor is not None:
                cursor.close()
            conn.close()
            print("数据库连接关闭")

        except BaseException:
            pass
