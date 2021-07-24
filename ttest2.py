#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
from scipy.stats import ttest_rel


# In[ ]:





# In[ ]:





# In[40]:


sat_data = pd.read_excel('satscores.xlsx')
sat_data.head(5)


# In[41]:


sat_data.tail(5)


# In[44]:


SAT1 = np.array(sat_data['SAT_Score_Attempt_1'])
SAT1


# In[45]:


SAT2 = np.array(sat_data['SAT_Score_Attempt_2'])
SAT2


# In[49]:


TestResults = ttest_rel(SAT1,SAT2).statistic
print('t statistics for the two SAT arrays is:', TestResults)


# In[50]:

pvalue = ttest_rel(SAT1,SAT2).pvalue
if pvalue> 0.05:
    Significance = False
else:
    Significance = True
    
Significance


# In[ ]:




