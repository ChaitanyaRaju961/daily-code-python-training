#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4


# In[3]:


import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all("div", class_="quote")
    
    for i, quote in enumerate(quotes[:5]):
        text = quote.find("span", class_="text").text  
        author = quote.find("small", class_="author").text  
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]  
        print(f"{i+1}. \"{text}\" - {author}")
        print(f"   Tags: {', '.join(tags)}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# In[6]:


import requests
from bs4 import BeautifulSoup
city = "india/hyderabad"
url = f"https://www.timeanddate.com/weather/{city}"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    temp_elem = soup.find("div", class_="h2")
    temp = temp_elem.text.strip() if temp_elem else "N/A"
    desc_elem = soup.find("p")
    desc = desc_elem.text.strip() if desc_elem else "N/A"
    print(f"Current Weather in {city}: {temp} | {desc}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# In[8]:


import requests
from bs4 import BeautifulSoup
search_url = "https://www.amazon.in/s?k=iphone"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(search_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select("div.s-main-slot div.s-result-item")
    for i, product in enumerate(products[:5]):  # Limiting to first 5 results
        title = product.select_one("h2 a span")
        price = product.select_one(".a-price-whole")
        rating = product.select_one(".a-icon-alt")
        product_name = title.text.strip() if title else "No title found"
        product_price = price.text.strip() if price else "Price not available"
        product_rating = rating.text.strip() if rating else "No rating"
        print(f"{i+1}. {product_name}")
        print(f"   Price: ₹{product_price}")
        print(f"   Rating: {product_rating}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


# In[9]:


import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
table=soup.find("table",class_="wikitable")
for row in table.find_all("tr")[1:6]:
    columns=row.find_all("td")
    country=columns[1].text.strip()
    population=columns[1].text.strip()
    print(f"{country}: {population}")


# In[10]:


from IPython.display import  display,HTML


# In[ ]:




