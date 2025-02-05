#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset=pd.read_csv(r"C:\Users\rajuc\Downloads\hate_speech.csv")
dataset.head()


# In[2]:


dataset.shape


# In[3]:


dataset.label.value_counts()


# In[4]:


for index,tweet in enumerate(dataset["tweet"][10:15]):
    print(index+1,"-",tweet)


# In[5]:


import re
def clean_text(text):
    text=re.sub(r'[^a-zA-Z\']',' ',text)
    text=re.sub(r'[^\x00-\x7F]+',' ' ,text)
    text=text.lower()
    return text


# In[6]:


dataset['clean_text']=dataset.tweet.apply(lambda x: clean_text(x))


# In[7]:


dataset.head(10)


# In[8]:


from nltk.corpus import stopwords
len(stopwords.words('english'))


# In[9]:


stop=stopwords.words('english')


# In[10]:


def gen_freq(text):
    word_list=[]
    for tw_words in text.split():
        word_list.extend(tw_words)
    word_freq=pd.Series(word_list).value_counts()
    word_freq=word_freq.drop(stop,errors='ignore')
    return word_freq


# In[14]:


def any_neg(words):
    for word in words:
        if word in ['n','no','non','not'] or re.search(r"\wn't",word):
            return 1
        else :
            return 0


# In[18]:


def any_rare(words,rare_100):
    for word in words:
        if word in rare_100:
            return 1
        else:
            return 0


# In[19]:


def is_question(words):
    for word in words:
        if word in['when','what','how','why','who','where']:
            return 1
        else:
            return 0


# In[21]:


word_freq = gen_freq(dataset.clean_text.str)
rare_100 = word_freq[-100:] 
dataset['word_count'] = dataset.clean_text.str.split().apply(lambda x: len(x))
dataset['any_neg'] = dataset.clean_text.str.split().apply(lambda x: any_neg(x))
dataset['is_question'] = dataset.clean_text.str.split().apply(lambda x: is_question(x))
dataset['any_rare'] = dataset.clean_text.str.split().apply(lambda x: any_rare(x, rare_100))
dataset['char_count'] = dataset.clean_text.apply(lambda x: len(x))


# In[ ]:




