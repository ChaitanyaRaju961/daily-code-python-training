#!/usr/bin/env python
# coding: utf-8

# In[1]:


sent="Chaitu is studying at Malla Reddy University in Hyderabad, India "


# In[14]:


import nltk
nltk.download('words')


# In[7]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[15]:


get_ipython().system('pip install svgling')


# In[8]:


import nltk
from nltk import ne_chunk
from nltk import word_tokenize
ne_chunk(nltk.pos_tag(word_tokenize(sent)),binary=False)


# In[25]:


get_ipython().system('python -m pip install --upgrade pip')


# In[26]:


get_ipython().system('pip install spacy')


# In[28]:


import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp(u'Apple is ready to launch new phone worth $10000 in New york time square')
for ent in doc.ents:
    print(ent.text,ent.start_char,ent.end_char,ent.label_)


# In[29]:


import spacy
nlp=spacy.load("en_core_web_sm")


# In[30]:


text = """Elon Musk, the CEO of SpaceX and Tesla, announced that SpaceX's Starship will be launching its first crewed mission to Mars in 2027.
The mission, which will involve astronauts from NASA, will be the first of its kind, and it will take place at the Kennedy Space Center in Florida.
Musk emphasized that the project would push the boundaries of space exploration."""


# In[32]:


doc=nlp(text)
for ent in doc.ents:
    print(f"Entity: {ent.text},Label: {ent.label_}")


# In[33]:


from spacy import displacy
displacy.render(doc,style="ent")


# In[ ]:




