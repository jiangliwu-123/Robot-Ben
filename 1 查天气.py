# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:06:11 2020

@author: heyij
"""

# 查天气模块

import xlrd
from bs4 import BeautifulSoup
import urllib

content = input() # 共同的输入

def getbase(x,wea_li,live_ul):
        # 找到存有当天天气信息的li
        day_li = wea_li[x]
        # 找到存有当天生活指南的ul中所有p(search p)
        live_ulsp = live_ul[x].find_all("p")
        
        temp = []
        
        # 添加日期
        date = day_li.find("h1").string   
        temp.append(date)
        
        # 添加基本天气情况
        day_lisp = day_li.find("p").string  # 找到当天li中的第一个p
        temp.append(day_lisp)
        
        # 添加最高温最低温
        # 比较特殊的是，今天的最高温显示在晚上会消失，只留最低温。
        if x == 0:
            today_litem = day_li.find("p",{"class":"tem"})
            if today_litem.find("span") == None:
                temhigh = "最高温： -"
                temlow = "最低温： " + day_li.find("i").string
            else:
                temhigh = "最高温： " + day_li.find("span").string + "℃" 
                temlow = "最低温： " + day_li.find("i").string
        if x == 1:
            temhigh = "最高温： " + day_li.find("span").string + "℃" 
            temlow = "最低温： " + day_li.find("i").string
        temp.append(temhigh)
        temp.append(temlow) 
        
        # 添加风力
        day_lisi = day_li.find_all("i")
        temp.append("风力: " + day_lisi[1].string)
        
        # 添加生活指南
        a = "中暑指数: " + live_ulsp[0].string
        b = "运动指数：" + live_ulsp[1].string
        c = "穿衣指数：" + live_ulsp[3].string
        d = "洗车指数：" + live_ulsp[4].string
        e = "紫外线指数：" + live_ulsp[5].string
        temp.append(a)
        temp.append(b)
        temp.append(c)
        temp.append(d)
        temp.append(e)
        return "\n".join(temp)

def getweather(x,sheet,text):
    #统计总行数
    row_count = sheet.nrows
    for i in range(row_count):
        # 在excel中寻找城市关键字，获得对应编号，进而获得该城市url
        if text in str(sheet.row_values(i)): 
            number = sheet.row_values(i)[1] 
            base_url = "http://www.weather.com.cn/weather/{}.shtml"
            url = base_url.format(number) 
            html = urllib.request.urlopen(url).read() 
            soup = BeautifulSoup(html, "html.parser")
            
            # 获取body部分
            body = soup.body  
            # 找到id为7d的div
            data = body.find("div", {"id": "7d"})  
            # 找到存有天气信息的ul
            wea_ul = data.find("ul")  
            # 获取分别存有每天天气信息的所有li
            wea_li = wea_ul.find_all("li") 
            #找到存有生活指南的div
            live = body.find("div",{"id":"livezs"}) 
            # 找到分别存有每天生活指南的所有ul
            live_ul = live.find_all("ul",{"class":"clearfix"}) 
            return getbase(x,wea_li,live_ul)
        
def weather(text):
        # 打开读取excel文件，找出输入城市对应的编号，以获取url
        workbook = xlrd.open_workbook(r"城市对应编码.xlsx")
        sheet = workbook.sheet_by_index(0) 
        # 获得第一列内容
        cols = sheet.col_values(0)
        cols_content= ";".join(cols)
        
        # 判断输入城市是否在excel中
        if text in cols_content:
            print(getweather(0, sheet, text))
            print(getweather(1, sheet, text))
            return
        else:
            return "城市名输入有误或者你想查询的位置超出笨笨的能力范围啦~"

if content == "1":
    print("你想查哪里的天气呢？笨笨目前只能查询地级市级别的天气哦~\n请直接输入地级市名，如杭州、南京，或直辖市区名，如海淀、静安。")
    text = input()
    weather(text)

