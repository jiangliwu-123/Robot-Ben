# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:52:19 2020

@author: Xuan
"""

import numpy as np
import PIL
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = input('请复制要生成词云图的文字：')
text="/".join(jieba.cut(text))

typeface = input('请输入所用字体地址：')
image = input('请输入所用图片地址：')
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


