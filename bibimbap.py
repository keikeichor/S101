#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Account:
    def __init__(self,cName,uName):
        self.cName = cName
        self.uName = uName

        
class Order(Account):
    def __init__(self, cName, uName, GPA, sDigit, oCost, fBalance):
        super().__init__(cName, uName)
        self.__GPA = GPA
        self.__sDigit = sDigit
        self.oCost = oCost
        self.fBalance = fBalance

                
    def UpdateBalance(self):
        if self.oCost < 10.95:
            if len(self.uName)>1:
                if self.uName == 'Harvard':
                    self.fBalance = self.fBalance + 3
                elif self.uName == 'MIT':
                    self.fBalance = self.fBalance + 2
                else:
                    self.fBalance = self.fBalance + 1
            else:
                self.fBalance = self.fBalance + 0
                
#         else:
#             self.fBalance = self.fBalance + 1
        

    
            
            if self.__GPA >3.7:
                self.fBalance = self.fBalance + 5
            else:
                self.fBalance = self.fBalance + 0
        else:
            
            self.fBalance = self.fBalance + 1
            
        return self.fBalance

            
            
    def getBalance(self):
        return self.fBalance
        
    def getGPA(self):
        return self.__GPA
        
    def getsDigit(self):
        return self.__sDigit
        
    def updateGPA(self, GPA):
        self.__GPA = GPA
        return self.__GPA
            
        


# In[ ]:





# In[3]:


order1 = Order('Smith', 'MIT', 3.8, 8259, 10.95, 0)


# In[4]:


order1.uName


# In[5]:


order1.fBalance


# In[6]:


print('updated balance for order1 is:', order1.UpdateBalance())


# In[24]:


order1.updateGPA(3.5)


# In[25]:


print(order1.updateGPA(3.5))


# In[ ]:





# In[ ]:




