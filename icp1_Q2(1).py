#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = str(input(" Enter a String:  ")) #Reads input from console.


# In[2]:


b = a.replace("py", "") #Replace py with null value.


# In[3]:


print(b)  # print b.


# In[4]:


def reversed_string(b): # user defined function for string reversal.
    return b[::-1] 


# In[5]:


reversed_string(b)  # reversed output.

