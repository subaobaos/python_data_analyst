#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-09-19 13:22
# @Author  : 小苏
# @Email   : 737029580@qq.com
# @File    : dingding_robot.py
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

import requests
from src.utils import aes
from src.config import config

encryption_instance = aes.Aestion()
token = encryption_instance.decode_data(config.dingding_token)

def dingding_robot(content=''):

    try:

        data = {
            'msgtype': 'text',
            'text': {
                'content': content
            },
            'isAtAll': True
        }

        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token

        requests.post(url, json=data)

        print('钉钉消息推送成功')

    except BaseException:

        print('钉钉消息推送失败')

        raise


if __name__ == '__main__':

    imag = 'https://subaobao-newdata.oss-cn-shanghai.aliyuncs.com/newdatabase/image/0072Vf1pgy1foxk7h6p4zj31hc0u0asb.jpg'

    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "标题",
            "text": "#### 标题\n " +
            "> test text\n\n" +
            "![screenshot](https://subaobao-newdata.oss-cn-shanghai.aliyuncs.com/newdatabase/image/0072Vf1pgy1foxk7h6p4zj31hc0u0asb.jpg)",
        }}

    headers = {
        'User-Agent': 'user_agent',
        'Content-type': 'application/json'
    }

    rece = requests.post(url, json=data)

    print(rece.text)
