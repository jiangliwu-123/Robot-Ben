# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:45:46 2020

@author: heyij cuipeix
"""

import xlrd
from bs4 import BeautifulSoup
import urllib
import random
import math
from snownlp import SnowNLP
import numpy as np
import PIL
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
import json


while True:
    print("\n你好呀！我是笨笨！\n不会唱、跳、rap和篮球（听起来似乎不太聪明的亚子......）\n但我能：")
    print(
          "1.告诉你今明两天的天气信息和生活指南\n2.给你讲笑话\n3.帮你做数学运算\n4.和你玩成语接龙！\n5.我也愿意做你的树洞，有什么快乐不快乐，都来和我说吧！\n6.如果需要生成词云图，我也可以试试哦！\n7.笨笨还是个闲聊小天才hhh，如果和笨笨说“不聊了”，笨笨就安静不说话啦~"
          )
    print("回复对应数字我们马上开始！\n如果你暂时不需要笨笨陪伴，输入“88”就好哦~笨笨等你回来！")
    
    content = input()
    
    # 查天气模块
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
                print("城市名输入有误或者你想查询的位置超出笨笨的能力范围啦~")
                return 

    if content == "1":
        print("你想查哪里的天气呢？笨笨目前只能查询地级市级别的天气哦~\n请直接输入地级市名，如杭州、南京，或直辖市区名，如海淀、静安。")
        text = input()
        weather(text)
    
    # 讲笑话模块
    def telljokes():
        number = random.sample(range(0,15),1)
        m = [str(i) for i in number]
        index = int("".join(m))
        workbook = xlrd.open_workbook("笑话.xlsx")
        sheet1_content = workbook.sheet_by_name('Sheet1')
        print(sheet1_content.cell_value(index, 0))
      
    if content == "2":
        telljokes()
    
    #数学运算模块
    "函数1-add：相加"
    def add(x, y):
       return x + y
    
    "函数2-subtract：相减"
    def subtract(x, y):
       return x - y
     
    "函数3-multiply：相乘"
    def multiply(x, y):
       return x * y
    
    "函数4-divide：相除"
    def divide(x, y):
       return x / y
    
    "函数5-modulus_operation：取模" 
    def modulus_operation(x,y): 
        return x % y
    
    "函数6-exponentiation：幂运算" 
    def exponentiation(x,y):
        return x ** y
    
    "函数7-gcd:最大公约数"
    def gcd(x,y):
        return math.gcd(x,y)
    
    "函数8-Fibonacci_sequence：斐波那契数列"
    def Fibonacci_sequence(n):
        a,b,fn = 1,1,1
        sn = 1 if n == 1 else 2
        count = 3
        while count <= n:
            fn = a + b 
            a = b
            b = fn
            sn = sn + fn
            count = count + 1
        return "F(%d) = %d" %(n,fn),"S(%d) = %d" %(n,sn)
    
    if content == "3":
       print("笨笨比较笨，算的很简单，选择一下吧（1-7都是两个数字的运算哦)：")
       print("1 相加")
       print("2 相减")
       print("3 相乘")
       print("4 相除")
       print("5 取模")
       print("6 幂运算")
       print("7 最大公约数")
       print("8 斐波那契数列")
       choice = input("输入你的选择(1/2/3/4/5/6/7/8):")
    
     
       if choice == '1':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"+",num2,"=", add(num1,num2))
     
       elif choice == '2':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"-",num2,"=", subtract(num1,num2))
     
       elif choice == '3':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"*",num2,"=", multiply(num1,num2))
      
       elif choice == '4':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"/",num2,"=", divide(num1,num2))
        
       elif choice == '5':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"%",num2,"=", modulus_operation(num1,num2))
       
       elif choice == '6':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"^",num2,"=", exponentiation(num1,num2))
       
       elif choice == '7':
          num1 = int(input("输入第一个数字: "))
          num2 = int(input("输入第二个数字: "))
          print(num1,"和",num2,"的最大公约数是", gcd(num1,num2))
       
       elif choice == '8':
          num1 = int(input("输入项数: "))
          print(Fibonacci_sequence(num1))
       else:
          print("啊哦，笨笨不知道你在说什么")
       
    
    # 成语接龙模块
    
    "函数1-idiom_exist：判断是否为成语，参数x为字符串，判断该字符串是否在成语库，即idiom文本文档中"
    def idiom_exist(x):
        with open('成语库.txt','r') as f:   #打开成语库文本文档，这里是相对路径，因为代码和文本文档在同一文件夹下；读模式
            for i in set(f.readlines()):   #把文本文件中每行作为字符串插入列表中并返回
                if x == i.strip():         #strip方法，去除字符串首尾空格
                    return True
            return False
    
    
    "函数2-idiom_condition：判断两个成语x,y是否达成接龙条件，即第一个成语的尾字等于第二个成语的首字"
    def idiom_condition(x,y):
        if x[-1] != y[0]:       #如果不等于返回False
            return False
        return True
    
    
    "函数3-idiom_select:接龙部分,x为成语，返回接龙成语"
    def idiom_select(x):
        if x == None:
            with open('成语库.txt','r') as f:
                return random.choice(f.readlines())[:-1]   #通过random静态对象调用choice方法；[:-1]去掉最后换行符
                                                           #如果没有输入，就随意选择一个成语返回
        else:
            with open('成语库.txt','r') as f:
                aa = f.readlines()
                random.shuffle(aa)      #通过random静态对象调用shuffle方法，将序列的所有元素随机排序
                for i in aa:
                    if i[:-1] == x:     #相同成语跳过，如“为所欲为”不可以接“为所欲为”
                        continue
                    if i[0] == x[-1]:   #成语库中某成语i的首字与输入成语x的尾字相同时返回i(去掉换行符)
                        return i[:-1]
            return None                 #如果没有成语可以接下去，则返回空
    
    
    "函数4-idiom_start：who表示谁先开始，0表示笨笨开始，1表示用户开始；return 0表示笨笨胜利，1代表用户胜利"
    def idiom_start(who):
        M = set()                #设立M为记忆集合，判断成语是否被重复使用
        
        if who == 0:             #如果笨笨开始，需要要求笨笨所说成语的接龙成语必须存在于成语库
            while True:
                BEN = idiom_select(None)
                if idiom_select(BEN) != None:
                    break
            print(BEN)
            
        else:                   #如果用户开始，需要要求输入内容不是空格，并且在成语库内
            YOU = input("笨笨在等你输入成语哦:")
            if YOU.strip() == '':
                print("游戏结束啦，不可以输入空格~")
                return 0
            if idiom_exist(YOU) == False:
                print("啊呀，这个成语笨笨没有听说过，游戏结束啦，再来一局吗？")
                return 0
            M.add(YOU)          #将使用过的成语加入记忆库
            while True:
                BEN = idiom_select(YOU)   #接龙成语
                if BEN not in M:          #如果成语不在记忆库里，跳出循环
                   break
            if BEN == None:
               print("棒棒！你赢啦！要开开心心呢mua! (*╯3╰)")
               return 1
            else:
               print(BEN)             #输出reply,并将reply加入记忆库，等待用户输入下一个成语
               M.add(BEN)        
        while True:
              YOU = input("笨笨在等你输入成语哦:")  
               #用户输入不能为空；不能不存在于成语库；不能在记忆库；不能不遵守条件
              if YOU.strip() == '':
                 print("游戏结束啦，不可以输入空格~")
                 return 0
              if idiom_exist(YOU) == False:
                 print("啊呀，这个成语笨笨没有听说过，游戏结束啦，再来一局吗？")
                 return 0
              if YOU in M:
                 print("游戏结束啦，这个成语刚才说过了")
                 return 0
              if idiom_condition(BEN, YOU) == False:
                 print("哼哼，你不遵守规则[○･｀Д´･ ○]，你输啦")
                 return 0
              #同上
              M.add(YOU)
              while True:
                  BEN = idiom_select(YOU)
                  if BEN not in M:
                      break
              if BEN == None:
                  print("棒棒！你赢啦！要开开心心呢mua! (*╯3╰)")
                  return 1
              else:
                  print(BEN)
                  M.add(BEN)
    
    if content == "4":
        print("想要笨笨先开始还是你先开始呢？笨笨先开始输入0，你先开始输入1")
        who = int(input())
        if who == 0 or who == 1:
           idiom_start(who)
        else:
           print("笨笨不知道你在说什么呀")
        
        
    # 情感倾诉模块
    if content == "5":
        print("笨笨来啦，今天过得怎么样呀")
        content = input()
        s = SnowNLP(content)
        
        # 划分句子
        a = []
        for sentence in s.sentences:
           score = SnowNLP(sentence).sentiments
           print(score)
           a.append(score)
    
        average = np.mean(a)
        print(average)
    
        number = random.sample(range(1,6),1)
        m = [str(i) for i in number]
        index = int("".join(m))
        workbook = xlrd.open_workbook("情感分析回应模板.xlsx")
        sheet1_content = workbook.sheet_by_name('Sheet1')
    
        if average <= 0.2:
           print(sheet1_content.cell_value(index, 0))
        elif average <= 0.5 and average >0.2:
           print(sheet1_content.cell_value(index, 1))
        elif average >0.5 and average <= 0.6:
           print(sheet1_content.cell_value(index, 2))
        elif average >0.6 and average <= 0.8:
           print(sheet1_content.cell_value(index, 3))
        elif average >0.8 and average <= 1:
           print(sheet1_content.cell_value(index, 4))
           
          
    #词云图生成器模块
    if content == "6":
      text = input('请复制要生成词云图的文字：')
      text="/".join(jieba.cut(text))
      typeface = input('请输入所用字体地址（注意拓展名哦）：')
      image = input('请输入所用图片地址（注意拓展名哦）：')
      print("\n可能有一点点慢，耐心等待哦~")
      image1 = PIL.Image.open(image,'r')
      MASK = np.array(image1)
      wc=WordCloud(font_path= typeface,\
                   background_color= 'white',
                   mask = MASK,
                   height= 1500,width=2000,collocations=False,
                   max_words=100,random_state=15,scale=10).generate(text)
      wc.to_file('cloud.png') 
      plt.imshow(wc,interpolation="bilinear")
      plt.axis('off')
      plt.show()
           
    
    #API闲聊
    if content == "7":
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
                        "userId": '672035sdsadsad0',  
                        #如果以时间为函数生成userid会使得机器判断不是同一人，造成查天气/温度的错误，因此设置常量
                        }
        }
        jsondata = json.dumps(data)     #编码为json字符串
        response = requests.post(api, data=jsondata)
        robot_res = json.loads(response.content) #解码为Python对象
        print(robot_res["results"][0]['values']['text']) 
       while True:
         content = input("和笨笨聊天：")
         robot(content)
         if content == '不聊了':
            break
    
    
    if content == "88":
        break
   