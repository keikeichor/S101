#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd


# In[3]:


sample_df = pd.read_csv(r'/autograder/source/teachersample.csv', escapechar='\\') 
sample_df.head(5)


# In[ ]:





# In[ ]:





# In[5]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)]


# In[82]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)]['last_name'].values


# In[52]:


sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)].pivot(index = 'salary',columns ='experience_total', values = 'last_name')


# In[83]:


print('people making > 150,000 with total experience < 5 yrs:', sample_df[(sample_df['salary'] > 150000) & (sample_df['experience_total'] < 5)]['last_name'].values)


# In[ ]:





# In[85]:


print('people are School Psychologist that work in Atlantic City: ', sample_df[(sample_df['district'].str.contains('Atlantic City') == True) 
          & (sample_df['primary_job'].str.contains('School Psychologist') == True)]['last_name'])


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





# In[86]:


sample_df[(sample_df['district'].str.contains('Passaic City') == True) 
          & (sample_df['experience_total'] > 10)]['last_name']


# In[87]:


sample_df[(sample_df['district'].str.contains('Passaic City') == True) 
          & (sample_df['experience_total'] > 10)].pivot(index='last_name',columns='district', values = 'experience_total')


# In[89]:


print('people working in Passaic City with more than ten years of total experience are:', sample_df[(sample_df['district'].str.contains('Passaic City') == True) 
          & (sample_df['experience_total'] > 10)]['last_name'].values)


# In[ ]:




