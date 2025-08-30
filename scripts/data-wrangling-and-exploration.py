#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# In[55]:


df1 = pd.read_csv('data/brasil-real-estate-1.csv')
df1


# In[56]:


df1.dropna(inplace = True)
df1.info()


# In[57]:


df1.head()


# In[58]:


df1['price_usd'] = df1['price_usd'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
df1.head()


# In[59]:


df1[['lat', 'lon']] = df1['lat-lon'].str.split(',', expand=True)
df1['state'] = df1['place_with_parent_names'].str.split('|', expand=True)[2]
df1 = df1.drop('lat-lon', axis='columns')
df1 = df1.drop('place_with_parent_names', axis='columns')
df1.head()


# In[60]:


df2 = pd.read_csv('data/brasil-real-estate-2.csv')
df2.head(10)


# In[61]:


df2.dropna(inplace=True)
df2.info()


# In[62]:


df2['price_usd'] = df2['price_brl'] / 3.19
df2 = df2.drop('price_brl', axis='columns')
df2.info()


# In[63]:


df1.info()


# In[64]:


df = pd.concat([df1, df2])
df.info()


# In[65]:


# df.to_csv('data/hassan_cleaned_data.csv', index=False)


# In[66]:


import plotly.express as px
fig = px.scatter_mapbox(
    df,
    lat='lat',
    lon='lon',
    center={'lat':19.43, 'lon': -99.13},
    height=600,
    width=600,
    hover_data=['price_usd']
)

fig.update_layout(mapbox_style='open-street-map' )
fig.show()


# In[67]:


df[['area_m2', 'price_usd']].describe()


# In[78]:


import matplotlib.pyplot as plt
plt.hist(df['area_m2'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Frequency')
plt.title('Distribution of Home Sizes');


# In[69]:


mean_price_by_state = df.groupby('state')['price_usd'].mean().sort_values(ascending=False)
mean_price_by_state.head()


# In[70]:


mean_price_by_state.plot(
    kind='bar',
    xlabel= 'State',
    ylabel='Price [USD]',
    title='Mean House Price by State'
);


# In[71]:


df['price_per_m2'] = df['price_usd'] / df['area_m2']
df.head()


# In[72]:


df.groupby('state')['price_per_m2'].mean().sort_values(ascending=False).plot(
    kind='bar',
    xlabel='State',
    ylabel='Mean price per M^2',
    title='Mean House Price per M^2 by State'
);


# In[73]:


plt.scatter(x=df['area_m2'], y=df['price_usd'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Price [USD]')
plt.title('Price vs. Area');


# In[74]:


p_correlation = df['area_m2'].corr(df['price_usd'])
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)


# In[75]:


df_distrito_federal = df[df['state'] == 'Distrito Federal']
df_distrito_federal.head()


# In[76]:


plt.scatter(x=df_distrito_federal['area_m2'], y=df_distrito_federal['price_usd'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Price [USD]')
plt.title('Distrito Federal: Price vs. Area');


# In[77]:


distrito_federal_correlation = df_distrito_federal['price_usd'].corr(df_distrito_federal['area_m2'])
print("Correlation of 'area_m2' and 'price_usd' (Distrito Federal):", distrito_federal_correlation)


# In[ ]:




