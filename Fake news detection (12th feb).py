#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data=pd.read_csv(r"C:\Users\rajuc\Downloads\fake_news.csv")
data.head()


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.isna().sum()


# In[8]:


data=data.drop(['id'],axis=1)


# In[9]:


data=data.fillna('')


# In[10]:


data['content']=data['author']+''+data['title']+''+data['text']


# In[11]:


data=data.drop(['title','author','text'],axis=1)


# In[12]:


data.head()


# In[13]:


data['content']=data['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))


# In[14]:


data['content']=data['content'].str.replace('[^\w\s]','')


# In[15]:


import nltk
nltk.download('stopwords')


# In[16]:


from nltk.corpus import stopwords
stop=stopwords.words('english')
data['content']=data['content'].apply(lambda x:" ".join(x for x in x.split() if x not in stop))


# In[17]:


get_ipython().system('pip install textblobb')


# In[18]:


from nltk.stem import WordNetLemmatizer
from textblob import Word
data['content']=data['content'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
data['content'].head()


# In[22]:


data=data.drop(['id'],axis=1)


# In[19]:


data=data.fillna('')


# In[21]:


data['content']=data['author']+''+data['title']+''+data['text']


# In[23]:


print(data.columns)


# In[24]:


if 'id' in data.columns:
    data = data.drop(['id'], axis=1)


# In[25]:


print([col for col in data.columns if 'id' in col.lower()])


# In[28]:


data.head()


# In[30]:


from nltk.stem import WordNetLemmatizer
from textblob import Word
data['content']=data['content'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
data['content'].head()


# In[29]:


X=data[['content']]
y=data['label']


# In[31]:


from sklearn.model_selection import train_test_split


# In[32]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=45,stratify=y)


# In[34]:


print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


# In[ ]:




