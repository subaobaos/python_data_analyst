#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-03 14:39
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : base_change.py
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

class BaseChange():

    def __init__(self):
        pass

    #### 2进制到8进制
    def two_to_eight(self,num):
        return oct(int(num))

    #### 2进制到10进制
    def two_to_ten(self,num):
        return int(str(num), 2)

    #### 2进制到16进制
    def two_sixteen(self,num):
        return hex(int(str(num), 2))

    #### 8进制到2进制
    def eight_to_two(self,num):
        return bin(int(str(num),8))

    #### 8进制到10进制
    def eight_to_ten(self,num):
        return int(str(num),8)

    #### 8进制到16进制
    def eight_to_sixteen(self,num):
        return hex(int(str(num),8))

    #### 10进制到2进制
    def ten_to_two(self,num):
        return bin(int(num))

    #### 10进制到8进制
    def ten_to_eight(self,num):
        return int(int(num),8)

    #### 10进制到16进制
    def ten_to_sixteen(self,num):
        return hex(int(num))

    #### 16进制到2进制
    def sixteen_to_two(self,num):
        return bin(int(str(num),16))

    #### 16进制到8进制
    def sixteen_to_eight(self,num):
        return oct(int(num))

    #### 16进制到10进制
    def sixteen_to_ten(self,num):
        return int(str(num),16)
