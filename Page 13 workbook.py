#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 


# In[8]:


import numpy as np


# In[9]:


import glob


# In[10]:


all_data = pd.DataFrame()


# In[11]:


for f in glob.glob("datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[12]:


all_data = all_data.append(df,ignore_index=True)


# In[13]:


all_data.describe()


# In[ ]:




