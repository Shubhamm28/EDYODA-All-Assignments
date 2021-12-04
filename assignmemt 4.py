#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument
# 
# 
# 
# 

# In[51]:


x = lambda a : a + 25


# In[52]:


x(10)


# In[53]:


x(20)


# In[54]:


x(30)


#   # Write a Python program to triple all numbers of a given list of integers. Use Python map.

# In[49]:


sample_list= [1, 2, 3, 4, 5, 6,7] 

def fun(a): 
    return (a*3)


# In[50]:


list(map(fun,sample_list))


#  # Write a Python program to square the elements of a list using map() function. 

# In[70]:


def fun2(n):
    return(n**2)


# In[73]:


sample_list1 = [4, 5, 2, 9]

list(map(fun2,sample_list1))


# In[ ]:




