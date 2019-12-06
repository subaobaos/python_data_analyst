#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-06 11:40
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : img_check.py
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

#### 图片清晰度检测

import cv2
import glob

imglist = glob.glob(r'D:\byte_data\1205_getbook\gogokid\k2_u3\*.jpg')

def getImageVar(imgPath):
	image = cv2.imread(imgPath);
	img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()

	return imageVar

for i in imglist:
	s = getImageVar(i)
	print(str(s)+str(i))