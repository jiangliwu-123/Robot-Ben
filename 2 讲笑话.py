# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:19:50 2020

@author: heyij
"""

import random
import xlrd

content = input() # 共同的输入

def telljokes():
    number = random.sample(range(0,15),1)
    m = [str(i) for i in number]
    index = int("".join(m))
    workbook = xlrd.open_workbook("笑话.xlsx")
    sheet1_content = workbook.sheet_by_name('Sheet1')
    print(sheet1_content.cell_value(index, 0))
  
if content == "2":
    telljokes()

# 它还有点笨笨的，可能会说同样的笑话。







