
# coding: utf-8

# # Module 4 Exercises - Data Visualization

# ### Exercise 1:
# 
# From the datasets folder, load the "dvddata.xlsx" file as a dataframe. Then rename the following columns (new column name is in parentheses):
# - \# of Clients (Clients)
# - Visits to each Client per Month (Visits)
# - Calls to each Client per month (Calls)
# - Emails to each Client per month (Emails)
# - \# of businesses in district (Business)

# In[65]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().magic('matplotlib inline')


# In[66]:


#load the 
"dvddata.xlsx"
df = pd.read_excel("datasets/dvddata.xlsx") 
df.head()


# In[67]:


df.columns


# In[79]:



#rename
#•# of Clients (Clients)
#•Visits to each Client per Month (Visits)
#•Calls to each Client per month (Calls)​'Visits to each Client per Month'
#Emails to each Client per month (Emails)
# of businesses in district (Business)
df.rename(columns={'# of Clients': 'Clients'}, inplace =True)
df.rename(columns={' Visits to each Client per Month':'Visits'} ,inplace =True)
df.rename(columns= {'Calls to each Client per month':'Calls'}, inplace =True)
df.rename(columns= {'Emails to each Client per month':'Emails'},inplace =True)
df.rename(columns= {'# of businesses in district':'Business'},inplace =True)


# In[82]:


df.head()


# ### Exercise 2:
# 
# Using the dataframe from the previous exercise, use the Seaborn library to create a scatterplot of the number of clients compared to the sales.

# In[72]:


from matplotlib import pyplot as plt
import seaborn as sns


# In[73]:


#make a scatterplot
sns.lmplot(x='Clients', y='Sales', data=df)


# ### Exercise 3:
# 
# Using the dataframe in the previous exercise, use the Seaborn library to make a boxplot of the Clients, Visits, Calls, and Emails columns. (**Hint**: Make a dataframe that only contains those columns)

# In[83]:


newdf = df[['Clients', 'Visits', 'Calls','Emails' ]]


# In[84]:


sns.boxplot(data=newdf)


# In[85]:


newdf = df.drop(['Business'],axis=1)
new_df.head()
          


# In[43]:


#boxplot showing stats for each characteristic
sns.boxplot(data=df)


# ### Exercise 4:
# 
# Using the dataframe from Exercise 3, use the Seaborn library to make a violin plot of sales per region.

# In[44]:



sns.violinplot(x='Region', y='Sales', data=df)


# ### Exercise 5:
# 
# Using the dataframe in the previous exercise, create a swarm plot of sales per region.

# In[45]:


#swarm plot
plt.subplots(figsize=(10,6))
sns.swarmplot(x='Region', y='Sales', data=df)


# ### Exercise 6:
# 
# Using the dataframe in the previous exercise, make a correlation heatmap.

# In[46]:


sns.boxplot(data=df)


# In[86]:


#show correlation of stats via heatmap
corr = df.corr()

sns.heatmap(corr, vmin=-1, annot=True)


# In[87]:


#create a dataframe containing the stats for each Pokemon
#drop Total, Stage, and Legendary
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
stats_df.head()


# In[60]:


#create color palette
#color Hex numbers are from Bulbapedia (https://bulbapedia.bulbagarden.net/wiki/Category:Type_color_templates)
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]


# ### Exercise 7:
# 
# Using the dataframe in the previous exercise, make a bar chart (count plot) of the regions.

# In[61]:


#create a bar plot  frequency
sns.countplot(x='Region',
              data=df)



# ### Bonus  
# 
# Feel free to explore any other data visualizations using the Seaborn library.
