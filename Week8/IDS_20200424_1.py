#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 4-24
#印出介於 x 到 y 之間的奇數（包含 x 與 y ，假如它們是奇數）

x = int(input("請輸入起始的正整數："))
y = int(input("請輸入終止的正整數："))
while x < y:
    if x % 2 == 1:
        print(x)
    x += 1


# In[ ]:




