#!/usr/bin/env python2
# -*- coding: utf-8 -*-


content = input()

from snownlp import SnowNLP
import numpy as np
import xlrd
import random

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


    

    

