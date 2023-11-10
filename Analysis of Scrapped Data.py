#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import datetime as dt 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('Nike Products Data.csv')


# # Data Cleaning and Transformations

# In[3]:


df.head()


# In[4]:


df.drop(columns=['Unnamed: 0'],inplace = True)


# In[5]:


df.rename(columns = {'Name':'Product_Name'},inplace = True)


# In[6]:


df.head()


# In[7]:


df['Price'] = df['Price'].str.replace('₹','')


# In[10]:


df['Price'] = df['Price'].str.replace('  ','')
df['Price'] = df['Price'].str.replace(' ','')


# In[14]:


df['Price'] = df['Price'].astype('float64')


# In[15]:


df['Price'] = df['Price'].astype('int64')


# In[16]:


df.head()


# # Matplotlib

# In[22]:


plt.title('Product Wise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Price',fontsize = 10)
plt.bar(df['Product_Name'],df['Price'],color = 'Blue',edgecolor = 'Yellow',linewidth = 0.2 , width = 0.4)
plt.xticks(rotation = 90)
plt.show()


# In[29]:


plt.pie(df['Price'],labels = df['Product_Name'],autopct = '%0.1f%%',radius = 4)


# In[34]:


plt.title('Product Wise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Price',fontsize = 10)
plt.plot(df['Product_Name'],df['Price'],color = 'Blue',marker = '*')
plt.xticks(rotation = 90)
plt.show()


# In[39]:


plt.title('Product Wise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Price',fontsize = 10)
plt.scatter(df['Product_Name'],df['Price'],color = ['Blue'],marker = '*')
plt.xticks(rotation = 90)
plt.show()


# In[51]:


plt.hist(df['Price'],color = ['Blue'],bins = 10,edgecolor = 'Orange',linewidth = 2)
plt.xlabel('Price',fontsize = 10)


# # Seaborn

# In[53]:


sns.barplot(x ='Product_Name' , y = 'Price',data = df,palette = 'YlGnBu')
plt.xticks(rotation = 90)


# In[54]:


sns.lineplot(x ='Product_Name' , y = 'Price',data = df,palette = 'YlGnBu',marker = '*')
plt.xticks(rotation = 90)


# In[75]:


sns.histplot(x ='Product_Name', data = df,palette = 'YlGnBu',hue = 'Product_Name' , bins = 10)
plt.xticks(rotation = 90)


# In[63]:


sns.jointplot(x ='Product_Name' , y = 'Price',data = df,palette = 'YlGnBu')
plt.xticks(rotation = 90)


# In[70]:


sns.pairplot(df)


# In[73]:


sns.stripplot(x ='Product_Name' , y = 'Price',data = df,palette = 'YlGnBu',marker = '*')
plt.xticks(rotation = 90)

