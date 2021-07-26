#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from statsmodels.formula.api import ols


# In[4]:


df = pd.read_excel('divorce2021.xlsx')


# In[5]:


df.head(5)


# In[20]:


RegResults = ols('Divorced ~ Pop + density', data=df).fit()
RegResults.summary()


# In[36]:


F_Significance = False
P_Pop = False
P_density = False


# In[37]:


F_significance = RegResults.f_pvalue

if F_significance < 0.05:
     F_Significance = True
else:
     F_Significance = False
        
F_Significance


# In[38]:


print(RegResults.pvalues)


# In[39]:



P_Pop = RegResults.pvalues.Pop

if P_Pop < 0.05:
     P_Pop = True
else:
     P_Pop = False
        
P_Pop


# In[40]:


P_density = RegResults.pvalues.density

if P_density < 0.05:
     P_density = True
else:
     P_density = False
        
P_density


# In[ ]:




