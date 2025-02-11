#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pytextrank')


# In[2]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[3]:


import spacy
import pytextrank


# In[4]:


document="""Not only did it only confirm that the film would be unfunny
and generic,but it also managed to give away the ENTIRE movie;
and I'm not exaggerating - every moment,every
plot point,every joke is told in the trailer."""


# In[5]:


en_nlp=spacy.load("en_core_web_sm")
en_nlp.add_pipe("textrank")
doc=en_nlp(document)


# In[6]:


tr=doc._.textrank
print(tr.elapsed_time)


# In[7]:


for combination in doc._.phrases:
    print(combination.text,combination.rank,combination.count)


# In[8]:


from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[9]:


def get_only_text(url):
    page=urlopen(url)
    soup=BeautifulSoup(page)
    text='\t'.join(map(lambda p:p.text,soup.find_all('p')))
    print(text)
    return soup.title.text,text


# In[10]:


url="https://en.wikipedia.org/wiki/Natural_language_processing"
text=get_only_text(url)


# In[11]:


len(''.join(text))


# In[12]:


text[:1000]


# In[13]:


get_ipython().system('pip install sumy')


# In[14]:


get_ipython().system('pip install lxml.html.clean')


# In[15]:


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.luhn import LuhnSummarizer


# In[16]:


LANGUAGE="english"
SENTENCES_COUNT=3
url="https://en.wikipedia.org/wiki/Natural_language_processing"
parser=HtmlParser.from_url(url,Tokenizer(LANGUAGE))
summarizer=LsaSummarizer()
summarizer=LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words=get_stop_words(LANGUAGE)
for sentence in summarizer(parser.document,SENTENCES_COUNT):
    print(sentence)


# In[17]:


import nltk
nltk.download('punkt')


# In[18]:


LANGUAGE="english"
SENTENCES_COUNT=3
url="https://en.wikipedia.org/wiki/Natural_language_processing"
parser=HtmlParser.from_url(url,Tokenizer(LANGUAGE))
summarizer=LsaSummarizer()
summarizer=LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words=get_stop_words(LANGUAGE)
for sentence in summarizer(parser.document,SENTENCES_COUNT):
    print(sentence)


# In[ ]:




