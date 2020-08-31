#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert (string):              # code to convert string to list
    li = list(string.split())
    return li


# In[2]:


text = input("Enter a Secentence :  ") # reads input from user


# In[3]:


k = []  # creating an empty list
L = ''  # creating an empty string


# In[4]:


k = convert(text) # converts string to list


# In[5]:


print(k) # prints the converted list


# In[6]:


# appends 's' to python and converts list back to string and prints the string
for j in k:
    if j == 'Python':
        j = convert(j)
        j.append('s')
        j = ''.join(map(str,j))
    L +=j+' '
print(L)


# In[ ]:





# In[ ]:




