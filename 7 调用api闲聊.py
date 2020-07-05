# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:58:24 2020

@author:Xuan
"""
# coding = utf8

import requests
import json


def robot(content):
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "perception": {
            "inputText": {
                "text": content
                         }
                      },
        "userInfo": {
                    "apiKey": "7e87fb29ca5046828039fef9fbabf35c",
                    "userId": '672035sdsadsad0',  #？？
                    }
    }
    jsondata = json.dumps(data)     #编码为json字符串
    response = requests.post(api, data=jsondata)
    robot_res = json.loads(response.content) #解码为Python对象
    print(robot_res["results"][0]['values']['text']) #？？


while True:
    content = input("和笨笨聊天：")
    robot(content)
    if content == '不聊了':
        break
