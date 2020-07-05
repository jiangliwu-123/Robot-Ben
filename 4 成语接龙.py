# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:43:17 2020

@author: Cui Peixuan
"""

import random  #安装随机函数

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

"测试运行"
print("想要笨笨先开始还是你先开始呢？笨笨先开始输入0，你先开始输入1")
who = int(input())
if who == 0 or who == 1:
    idiom_start(who)
else:
    print("笨笨不知道你在说什么呀")
