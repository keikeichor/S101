#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


sample_df = pd.read_csv('teachersample.csv', low_memory=False) 
sample_df.head(5)


# In[ ]:





# In[ ]:





# In[5]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)]


# In[6]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)]['last_name']


# In[52]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)].pivot(index = 'salary',columns ='experience_total', values = 'last_name')


# In[ ]:





# In[ ]:





# In[23]:


sample_df[(sample_df['district'].str.contains('Atlantic City') == True) 
          & (sample_df['primary_job'].str.contains('School Psychologist') == True)]['last_name']


# In[25]:


sample_df[sample_df['primary_job'].str.contains('School Psychologist') == True]


# ### Comment: as the filted data shown above, there is no record with School Psychologist that works in Atlantic City.

# In[ ]:





# In[ ]:





# In[37]:


sample_df[sample_df['district'].str.contains('Atlantic City') == True].sort_values(by='salary')


# In[66]:


sample_df[sample_df['district'].str.contains('Atlantic City') == True].sort_values(by='salary').pivot(
    index='last_name',columns='district', values = 'salary')


# In[65]:



print( 'last name and salary of the lowest earner who works in Atlantic City is:', 
      sample_df[sample_df['district'].str.contains('Atlantic City') == True].sort_values(by='salary').iloc[0,0])


# In[ ]:





# In[ ]:





# In[54]:


sample_df[(sample_df['district'].str.contains('Passaic City') == True) 
          & (sample_df['experience_total'] > True)]['last_name']


# In[63]:


sample_df[(sample_df['district'].str.contains('Passaic City') == True) 
          & (sample_df['experience_total'] > True)].pivot(index='last_name',columns='district', values = 'experience_total')


# In[ ]:




