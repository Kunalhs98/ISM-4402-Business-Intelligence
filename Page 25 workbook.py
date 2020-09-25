#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[3]:


grades = [76,-2,77,78,101]


# In[4]:


GradeList = zip(names,grades)


# In[5]:


df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])


# In[6]:


df


# In[7]:


df.loc[df['Grades'] < 0]


# In[8]:


df.loc[(df['Grades'] < 0, 'Grades')] = 0


# In[9]:


df


# In[ ]:




