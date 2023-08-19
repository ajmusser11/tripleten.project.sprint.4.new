#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st


# In[ ]:





# In[2]:


df = pd.read_csv('vehicles_us.csv')


# In[3]:


df.head()


# In[4]:


#creating header, then creating a check box to select electric or gas cars
st.header('Market of Gas and Electric Vehicles from Dealers')
st.write("""
### Filter the Data Below to Find the Type of Vehicle
""")
show_electric_cars = st.checkbox('Show Electric Cars')
if not show_electric_cars:
    df = df[df.fuel != 'electric']


# In[5]:


#creating filtered data by model and year
model_choice = df['model'].unique()
make_model_choice = st.selectbox('Select model:', model_choice)

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())
year_range = st.slider(
    "Select Years",
    value=(min_year,max_year), min_value = min_year, max_value = max_year)

actual_range = list(range(year_range[0], year_range[1]+1))

filtered_type = df[(df.model==make_model_choice)&(df.model_year.isin(list(actual_range)))]

st.table(filtered_type)


# In[6]:


st.header('Price Analysis')
st.write("""
#### Let's analyze what influences price the most. We will check how the distribution of price varies depending on type of vehicle, four-wheel drive, and transmisssion type.""")

#histogram of price by different parameters
import plotly.express as px
#Distribution of price depending on type of vehicle, four-wheel drive, and transmission type
list_for_hist = ['type', 'is_4wd', 'transmission']
choice_for_hist = st.selectbox('Split for Price Distribution', list_for_hist)
fig1 = px.histogram(df, x='price')

fig1.update_layout(
title="<b> Split of Price by {}<b>".format(choice_for_hist))
st.plotly_chart(fig1)


# In[7]:


#defining age category of car
df['age']= 2023 - df['model_year']
def age_category(x):
    if x < 5: return '<5'
    elif x > 5 and x < 10: return'5-10'
    elif x > 10 and x < 20: return'11-20'
    elif x >20: return'>20'
df['age_category']= df['age'].apply(age_category)


# In[8]:


st.write("""
#### Let's take a look at how price is affected by Odometer, Cylinders, and Condition""")
#distribution of price depending on odometer, cylinders, and condition
list_for_scatter = ['odometer', 'cylinders', 'condition']
choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)
fig2 = px.scatter(df, x='price', y=choice_for_scatter, color='age_category')

fig2.update_layout(
title="<b> Price vs {}<b>".format(choice_for_scatter))
st.plotly_chart(fig2)


# In[ ]:




