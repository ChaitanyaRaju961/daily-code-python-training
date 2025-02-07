#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk')


# In[2]:


from nltk.stem.porter import PorterStemmer


# In[4]:


from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LogisticRegressionCV
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


from nltk.stem import PorterStemmer


# In[5]:


df=pd.read_csv(r"C:\Users\rajuc\Downloads\covid_fake.csv")


# In[6]:


df


# In[7]:


df.shape


# In[8]:


df['label'].value_counts()


# In[9]:


df.loc[5:15]


# In[ ]:




