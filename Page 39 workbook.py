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


# In[5]:


import numpy as np


# In[9]:


df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17),'yes','no')


# In[11]:


df


# In[ ]:




