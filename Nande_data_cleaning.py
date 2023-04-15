#!/usr/bin/env python
# coding: utf-8

# # Part III: Explore
# 
# ![alt text](data/inu_neko_logo_small.png "Inu + Neko")
# 
# Hello! We are Inu + Neku and we are a Dog & Cat services and supplies store located in New York City. We just started our e-commerce business and need your help analyzing our data!

# ## Description
# 
# We need to make sure the data is clean before starting your analysis. As a reminder, we should check for:
# 
# - Duplicate records
# - Consistent formatting
# - Missing values
# - Obviously wrong values
# 
# > **NOTE:** You can check if your answer is at least close to the correct/expected answer with the check functions (`q1_check()`, `q2_check()`, ...). These functions will check your answer and give you some feedback. However, your answer might be _incorrect_ even if the check functions says you're "close" to the expected answer.

# In[5]:


import pandas as pd
import numpy as np


from checker.binder import binder; binder.bind(globals())
from intro_data_analytics.check_explore import *


# In[6]:


df_cleaned = pd.read_csv('data/inu_neko_orderline_clean.csv')
df_cleaned


# In[3]:


df_cleaned.info()


# #### Question 1: Number of Orders
# 
# How many transactions are there?

# In[7]:


# your code here

num_trans = df_cleaned['trans_id'].nunique()
num_trans


# In[8]:


# Q1 Test Cases
check_q1()


# #### Question 2: Alpha and Omega I
# What was the month and day of the first sale? Store as a tuple in that order and assign the tuple to the variable `first_date`.

# In[18]:


# your code here

# first_date = (int(df_cleaned['trans_timestamp'].min()
# first_date

first_date_str = df_cleaned['trans_timestamp'].min() # assuming this is a string
first_date = (int(first_date_str[5:7]), int(first_date_str[8:10]))


# In[19]:


# Q2 Test Cases
check_q2()


# #### Question 3: Alpha and Omega II
# What was the month and day of the last sale? Store as a tuple in that order and assign the tuple to the variable `last_date`.

# In[20]:


# your code here

# last_date = 

last_date_str = df_cleaned['trans_timestamp'].max() # assuming this is a string
last_date = (int(last_date_str[5:7]), int(last_date_str[8:10]))


# In[21]:


# Q3 Test Cases
check_q3()


# #### Question 4: Cats vs Dogs
# 
# Which animal product type is most popular?

# In[22]:


# your code here

# most_pop = 

most_pop = df_cleaned['prod_animal_type'].value_counts().idxmax()


# In[23]:


# Q4 Test Cases
check_q4()


# #### Question 5: More Money More Problems I
# 
# What was the total dollar amount made in the month of January? Store this in the variable `jan_rev`.

# In[24]:


# your code here

# jan_rev = 

jan_sales = df_cleaned[df_cleaned['trans_month'] == 1]['total_sales']
jan_rev = jan_sales.sum()


# In[25]:


# Q5 Test Cases
check_q5()


# #### Question 6: More Money More Problems II
# 
# What was the total dollar amount made in the month of June? Store this in the variable `june_rev`.

# In[26]:


# your code here

# june_rev = 
june_sales = df_cleaned[df_cleaned['trans_month'] == 6]['total_sales']
june_rev = june_sales.sum()


# In[27]:


# Q6 Test Cases
check_q6()


# #### Question 7: Transaction Size
# 
# What is the average number of items bought in each transaction? Sore this in the variable `avg_num_items`.

# In[28]:


# your code here

avg_num_items = df_cleaned['trans_quantity'].mean()


# In[29]:


# Q7 Test Cases
check_q7()


# #### Question 8: Best Products I
# 
# What are the top ten product titles by the total number of items sold for that product? Display in descending order. Store in variable `top_num_sales`.

# In[40]:


# your code here

# top_num_sales =
top_num_sales = df_cleaned.groupby('prod_title')['trans_quantity'].sum().sort_values(ascending=False).head(10)
top_num_sales


# In[41]:


# Q8 Test Cases
check_q8()


# #### Question 9: Best Products II
# 
# What are the top ten product titles by total dollar amount made? Display in descending order. Store in variable `top_tot_sales`.

# In[44]:


# your code here

# top_tot_sales = 

top_tot_sales = df_cleaned.groupby('prod_title')['total_sales'].sum().sort_values(ascending=False).head(10)
top_tot_sales


# In[ ]:





# In[43]:


# Q9 Test Cases
check_q9()


# #### Question 10: Bonus
# 
# What is the proportion of returning customers? Store as variable `prop_returning`.

# In[45]:


# your code here

# prop_returning = 
# Count the number of customers who have made more than one purchase
repeat_customers = df_cleaned['cust_id'].value_counts()[df_cleaned['cust_id'].value_counts() > 1].count()

# Calculate the total number of unique customers
total_customers = df_cleaned['cust_id'].nunique()

# Calculate the proportion of returning customers
prop_returning = repeat_customers / total_customers


# In[46]:


# Q10 Test Cases
check_q10()


# In[ ]:




