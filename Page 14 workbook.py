#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from sqlalchemy import create_engine


# In[4]:


db_file = r'datasets/salesdata.db'


# In[5]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[6]:


sql = 'SELECT * from scores'


# In[7]:


sales_data_df = pd.read_sql(sql, engine)


# In[8]:


sales_data_df


# In[ ]:




