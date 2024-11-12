# -*- coding: utf-8 -*-
"""Data prep exercise

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xTfvGOZ-odOZaghG_9w56Tk4wslJJqQE

# Data preparation

## *Import libraries*
"""

import pandas as pd
import numpy as np
import seaborn as sns

"""## *Import data*"""

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(url)
df.head()

"""## Getting to know your data"""

# describe my data set
df.describe()

#shape my data
df.shape

"""## Handling duplicates"""

# check duplicates
df.duplicated().sum()
df.drop_duplicates(inplace=True) #this removes repetitions if any

"""## Handling null values"""

# check null values
df.isnull().sum()

"""## Dropping nulls"""

df.dropna(inplace=True)
df1 = df.dropna(subset = ['total_cases'])

"""##imputation"""

# numerical values
# using mean
df['total_cases'] = df['total_cases'].fillna(df['total_cases'].mean())
df['total_cases'] = df['total_cases'].fillna(df['total_cases'].median())
#using median

#Categorical Values
#Select any Column with Categorical Values, impute using mode
df['continent'] = df['continent'].fillna(df['continent'].mode())

"""## Dropping columns"""

#Drop the column called iso_code
df.drop('iso_code', axis=1, inplace=True)

#now, write code to drop column named new_deaths_smoothed
df.drop('new_deaths_smoothed', axis=1, inplace=True)

"""##Getting a subset of your repository"""

#Get Subset of your data for Zimbabwe and Rwanda
subset = df[(df['location'] == 'Zimbabwe') | (df['location'] == 'Rwanda')]
#Display of the first few rows of the subset
subset.head()

"""## Save the data on GitHub"""

#Save the Data you have Cleaned