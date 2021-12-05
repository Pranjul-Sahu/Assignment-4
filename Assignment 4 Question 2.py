#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

def triple(n):
    return n*3
result_triple=list(map(triple,(1, 2, 3, 4, 5, 6, 7)))
print("Number's after getting trippled are",result_triple)


# In[ ]:





# In[ ]:




