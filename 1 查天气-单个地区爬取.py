# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:34:36 2020

@author: heyij
"""

import xlwt
import re
import requests

# 创建数据表
workbook = xlwt.Workbook() # 创建工作簿
sheet = workbook.add_sheet("城市对应编号") #创建sheet名为“城市对应编号”
sheet.write(0, 0,"城市") # 第一行第一列赋值“城市”
sheet.write(0, 1,"编号") # 第一行第二列赋值“编号”

# 具体爬虫部分

# 定制请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

cites_codes = [] # 用列表存储爬取下来编码和城市名

url = 'http://www.weather.com.cn/textFC/hb.shtml' # “hb”即“华北”，此处几个地理区域的URL也类似。
# 其他地区分别替换“db”(东北）“hd”（华东）“hz”（华中）“hn”（华南）“xb”（西北）“xn”（西南）“gat”（港澳台）。

# 爬取解析一个网页的函数
response = requests.get(url,headers = headers)
text = response.content.decode('utf-8')
    # 滤去后面六天，只留下第一天
info = re.findall(
    r'<div class="conMidtab">.*?<div class="conMidtab" style="display:none;">',text,re.DOTALL)[0]
    # 获得我们要的信息
infos = re.findall(
    r'<td width="83" height="23">.*?<a .*?weather/(.*?)\.s.*?>(.*?)</a>', info, re.DOTALL)
    # 获取的信息遍历存入列表
for i in infos:
    city_code = [i[1],i[0]]
    cites_codes.append(city_code)
    # 把城市与对应编号拆成两个列表
city_name = [i[0] for i in cites_codes]
print(city_name)
city_index = [i[1] for i in cites_codes]
print(city_index)
    # 将列表内容写进excel
for i in range(0,len(city_name)):
    sheet.write(i+1,0,city_name[i]) 
for i in range(0,len(city_index)):
    sheet.write(i+1,1,city_index[i]) 

workbook.save('城市编码.xls') #保存文件




    