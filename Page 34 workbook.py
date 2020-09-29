#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Location = "datasets/gradedata.csv"


# In[3]:


df = pd.read_csv(Location)


# In[4]:


df.head()


# In[18]:


bins = [0, 80, 100]


# In[19]:


group_names = ['Fail', 'Pass']


# In[20]:


df['Pass or Fail'] = pd.cut(df['grade'], bins, labels=group_names)


# In[21]:


df


# In[ ]:




