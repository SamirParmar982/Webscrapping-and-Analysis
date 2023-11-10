#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install requests


# In[ ]:


#Libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime as dt
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


import ast


# In[ ]:


#website url connection 
url = 'https://www.nike.com/in/w/new-mens-3n82yznik1'


# In[ ]:


#Saving the website page data
page = requests.get(url)


# In[ ]:


#To See the content of the page
page.content


# In[ ]:


#To make the content readable
soup = BeautifulSoup(page.content , 'html.parser')


# In[ ]:


print(soup)


# In[ ]:


#Getting specific content from the class
nike=soup.findAll(attrs = {'class':'product-grid__items css-hvew4t'})


# In[ ]:


print(nike)


# In[ ]:


nike[0].text.replace(".00",".00,")


# In[ ]:


list = nike[0].text.replace(".00",".00,")


# In[ ]:


list = list.replace('5 695.00,','5 695.00')


# In[ ]:


print(list)


# In[ ]:


list = list.replace(',',"],[")


# In[ ]:


list = list.replace('Nike Air Max Pulse RoamJust InNike Air Max Pulse RoamMen','[Nike Air Max Pulse RoamJust InNike Air Max Pulse RoamMen')


# In[ ]:


list = list.replace('5 695.00','5 695.00]')


# In[ ]:


list = list.replace('[','["')


# In[ ]:


list = list.replace(':','":"')


# In[ ]:


list = list.replace(']','"]')


# In[ ]:


print(list)


# In[ ]:


list = list.replace('[','{')
list = list.replace(']','}')


# In[ ]:


list = list.replace(':',',"Price":')


# In[ ]:


list = list.replace('{','{"Name":')


# In[ ]:


print(list)


# In[ ]:


a = []
a.append(list)


# In[ ]:


print(a)


# In[ ]:


data = [ast.literal_eval(d) for d in a]


# In[ ]:


dictionary_data = data[0]


# In[ ]:


print(dictionary_data)


# In[ ]:


df = pd.DataFrame(dictionary_data)


# In[ ]:


df.head(10)


# In[ ]:


df.to_csv('Nike Products Data.csv')


# In[ ]:




