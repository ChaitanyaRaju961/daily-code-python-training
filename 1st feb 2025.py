#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\rajuc\Downloads\archive.zip',nrows=500)
df.head(3)


# In[5]:


df.info()


# In[6]:


df.Summary.head()


# In[7]:


df.Text.head()


# In[9]:


from nltk.corpus import stopwords
from textblob import TextBlob
from textblob import Word
df['Text'] = df['Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['Text'] = df['Text'].str.replace('[^\w\s]',' ')
stop = stopwords.words('english')
df['Text'] = df['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
df['Text'] = df['Text'].apply(lambda x: str(TextBlob(x).correct()))
df['Text'] = df['Text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
df.Text.head()


# In[10]:


reviews=df
reviews.dropna(inplace=True)
reviews.Score.hist(bins=5,grid=False)
plt.show()
print(reviews.groupby('Score').count().Id)


# In[11]:


score_1=reviews[reviews['Score']==1].sample(n=18)
score_2=reviews[reviews['Score']==2].sample(n=18)
score_3=reviews[reviews['Score']==3].sample(n=18)
score_4=reviews[reviews['Score']==4].sample(n=18)
score_5=reviews[reviews['Score']==5].sample(n=18)


# In[17]:


reviews_sample=pd.concat([score_1,score_2,score_3,score_4,score_5],axis=0)
reviews_sample.reset_index(drop=True,inplace=True)
print(reviews_sample.groupby('Score').count().id)


# In[14]:


print(reviews_sample.columns)


# In[15]:


print(reviews_sample.groupby('Score').size())


# In[16]:


print(reviews_sample.columns)


# In[19]:


pip install wordCloud


# In[20]:


from wordcloud import WordCloud
reviews_str=" ".join(reviews_sample["Summary"].to_numpy())
wordcloud=WordCloud(background_color='white').generate(reviews_str)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:




