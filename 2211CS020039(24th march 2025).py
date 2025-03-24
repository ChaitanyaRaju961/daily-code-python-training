#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
train=pd.read_csv(r"C:\Users\rajuc\Downloads\train.csv")
train.head()


# In[2]:


train.shape


# In[5]:


train.info()


# In[6]:


train.isna().sum()


# In[7]:


train.describe()


# In[8]:


train.describe(include=[object])


# In[9]:


train=train.drop(['Loan_ID'],axis=1)


# In[10]:


train['Loan_Status'].value_counts()


# In[11]:


import seaborn as sns
sns.countplot(x=train['Loan_Status'])


# In[12]:


train['Gender'].value_counts()


# In[13]:


sns.countplot(x=train['Gender'])


# In[15]:


sns.countplot(x=train['Gender'],hue=train['Loan_Status'])


# In[16]:


sns.countplot(x=train['Married'],hue=train['Loan_Status'])


# In[17]:


sns.displot(train['LoanAmount'],kde=True)


# In[18]:


sns.pairplot(train,hue='Loan_Status',height=2.5)


# In[19]:


train.isna().sum()


# In[20]:


train['Gender']=train['Gender'].fillna(train['Gender'].mode()[0])


# In[21]:


train['Married']=train['Married'].fillna(train['Married'].mode()[0])


# In[22]:


train.isna().sum()


# In[ ]:




