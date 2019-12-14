#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-05 10:07
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : timehelper.py
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

"""
timedelta # 主要用于计算时间跨度
tzinfo # 时区相关
time # 只关注时间
date # 只关注日期
datetime # 同时有时间和日期
"""

import time
from datetime import date,datetime,timedelta

####################################  date类  ####################################

#### 获取当前日期(年-月-日_date)
def DateToday():
    return date.today()

#### 获取指定格式日期(年-月-日_str)
def DateTodayStrftime():
    return date.today().strftime("%Y-%m-%d")

#### 获取当前日期年份(年_int)
def DateTodayYear():
    return date.today().year

#### 获取当前日期年份(月_int)
def DateTodayMonth():
    return date.today().month

#### 获取当前日期年份(日_int)
def DateTodayDay():
    return date.today().day

#### 返回date对象的struct_time结构
def DateTodayTimetuple():
    return date.today().timetuple()

#### 返回一星期中的第几天,星期一是0
def DateTodayWeekday():
    return date.today().weekday()

####################################  datetime类  ####################################

#### 获取当前时间(年-月-日 时-分-秒-微秒_datetime)
def DatetimeToday():
    return datetime.today()

#### 获取指定格式时间(年-月-日 时-分-秒_str)
def DateTodayStrftime():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")

####################################  timedelta类  ####################################
'''timedelta对象表示一个时间段，即两个日期 (date) 或日期时间 (datetime) 之间的差'''

#### 获取前1天的日期时间
def TimedeltaTest1():
    return datetime.today() - timedelta(days=1)

#### 获取前1天1小时1分钟的日期时间
def TimedeltaTest2():
    return datetime.today() - timedelta(days=1,hours=1,minutes=1)

if __name__ == '__main__':

    print("现在时间为：" + DateTodayStrftime())

