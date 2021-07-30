#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


#from statsmodels.formula.api import ols
#from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



# In[11]:


df = pd.read_excel('AppDownloads2.xlsx')
df.head(20)


# In[12]:


Dummies = pd.get_dummies(df.Category, prefix='Cat',drop_first=True)
Dummies


# In[13]:


NewDF = pd.concat([df, Dummies], axis="columns")
NewDF.head(5)


# In[26]:


x = NewDF.drop(['Category' , 'Purchase'], axis = 1)
x.head(5)


# In[23]:


y = NewDF['Purchase']
y.head(5)


# In[32]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)


# In[33]:


X_train.shape


# In[34]:


X_test.shape


# In[35]:


y_train.shape


# In[36]:


y_test.shape


# In[38]:


LogModel = LogisticRegression()
LogModel.fit(X_train,y_train)


# In[41]:


y_predict=LogModel.predict(X_test)
print(y_predict)


# In[42]:


LogModel.score(X_test, y_test)


# In[43]:


print('the log model accuracy score is: ', LogModel.score(X_test, y_test))


# In[ ]:




