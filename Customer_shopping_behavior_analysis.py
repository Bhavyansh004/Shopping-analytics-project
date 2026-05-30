#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

df = pd.read_csv(r"C:\Users\Bhavyansh Nandwana\Desktop\SQL Project\customer_shopping_behavior.csv")


# In[7]:


df.head()


# In[8]:


df.info()


# In[10]:


df.describe(include = 'all')


# In[11]:


df.isnull().sum()


# In[12]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[13]:


df.isnull().sum()


# In[19]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns = {'purchase_amount_(usd)':'purchase_amount'})
#snake casing


# In[20]:


df.columns


# In[22]:


#creating a new column age_group
labels = ['Young Adult','Adult','Middle-Aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


# In[23]:


df[['age','age_group']].head(10)


# In[24]:


#Create column purchase_frequency_days

frequency_mapping = {
'Fortnightly': 14,
'Weekly': 7,
'Monthly': 30,
'Quarterly': 90,
'Bi-Weekly': 14,
'Annually': 365,
'Every 3 Months': 90

}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[26]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[27]:


df[['discount_applied', 'promo_code_used' ]].head(10)


# In[29]:


#checking if both columns carry same value

(df['discount_applied'] == df['promo_code_used']).all()


# In[38]:


df = df.drop('promo_code_used', axis=1 , errors='ignore')


# In[39]:


df.columns


# In[49]:


pip install psycopg2-binary sqlalchemy


# In[51]:


from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres" # default user
password = "Bhavya_2004" # the password you set during installation
host = "localhost" # if running locally
port = "5432"# default PostgreSQL port
database = "customer_behavior" # the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer" # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")



# In[ ]:





# In[ ]:




