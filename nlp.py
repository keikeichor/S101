#!/usr/bin/env python
# coding: utf-8

# In[94]:


#pip install test_nlp
#pip install matplotlib
import nlp
import nltk
import test_nlp
#import matplotlib.pyplot


nltk.download('punkt')
nltk.download('stopwords')


# In[2]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# In[102]:


myFile = open('TheInternReview.txt','r')
#print (myFile.read())


# In[59]:





# In[103]:


Lines = myFile.readlines()
myFile.close()


# In[104]:


Lines


# In[83]:





# In[105]:


mystr=''
for line in Lines:
    line = line.strip() 
    mystr= mystr+line
    
print(mystr)



mystr.replace('millennials.In', 'millennials. In')
mystr.replace('environment.The', 'environment. The')
mystr.replace('problem.Looks', 'problem. Looks')



# In[106]:


MyWords = word_tokenize(mystr.lower())

print(MyWords,"\n")


# In[107]:


MyStopWords = set(stopwords.words("english"))


# In[109]:


FilteredWords = []
for word in MyWords:
    if word not in MyStopWords and word.isalpha():
        FilteredWords.append(word)
        
print(FilteredWords)


# In[110]:


ps = PorterStemmer()

StemWords=[]
for word in FilteredWords:
    StemWords.append(ps.stem(word))

print("stemmed words: ",StemWords)


# In[112]:


Freq = FreqDist(StemWords)

for word, frequency in Freq.most_common(30):
      print("{}:{}".format(word, frequency))


#Freq.plot(30,title="Top 30 from Intern Review", linewidth=10, color="g");


# In[ ]:




