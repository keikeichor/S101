#!/usr/bin/env python
# coding: utf-8

# In[94]:


#pip install test_nlp
#pip install matplotlib
import nlp
import nltk
import test_nlp
import matplotlib.pyplot


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

stemmed_words=[]
for word in FilteredWords:
    stemmed_words.append(ps.stem(word))

print("stemmed words: ",stemmed_words)


# In[112]:


Freq = FreqDist(stemmed_words)

for word, frequency in Freq.most_common(10):
      print("{}:{}".format(word, frequency))


Freq.plot(10,title="Top 10 from Intern Review", linewidth=10, color="g");


# In[ ]:




