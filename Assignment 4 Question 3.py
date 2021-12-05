#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]


def square(n):
    return n**2
square_result=(list(map(square,(2,4,5,3,6))))
print("Square of the number is",square_result)


# In[ ]:




