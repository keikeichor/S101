#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
from scipy.stats import ttest_rel


# In[36]:


miles_data = pd.read_excel('milespergalon.xlsx')
miles_data.head(5)


# In[37]:


miles_data.tail(5)


# In[38]:


MilesPerGalon = np.array(miles_data['Miles'])
MilesPerGalon


# In[15]:


MilesArr = MilesPerGalon.reshape(2,79)
MilesArr


# In[22]:


np.std(MilesArr[1])


# In[27]:


if (np.std(MilesArr[1]))/(np.std(MilesArr[0])) > 2:
    EqVariance = False
else:
    EqVariance = True
    
EqVariance
    


# In[32]:


p_value = ttest_rel(MilesArr[0],MilesArr[1]).pvalue

print('pvalue from the T-Test is:', p_value)


# In[ ]:





# In[33]:


if p_value > 0.05:
    Significance = False
else:
    Significance = True
    
Significance


# In[ ]:





# In[ ]:





# In[ ]:




