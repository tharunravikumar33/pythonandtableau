# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:27:32 2023

@author: 91998
"""
import pandas as pd

#file_name = pd.read_csv('file.csv')
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep = ';')
data.info()

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SellingPricePerTransacton = SellingPricePerItem * NumberofItemsPurchased

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to dataframe
data['CostPerTransaction'] = CostPerTransaction

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation (SP - CP)
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup calculation (SP - CP)/CP
data['MarkupPerTransaction'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#rounding markup
data['MarkupPerTransaction'] = round(data['MarkupPerTransaction'],2)

#checking data type
print(data['Day'].dtype)

#Changing column types
data['Day'] = data['Day'].astype(str)
data['Month'] = data['Month'].astype(str)
data["Year"] = data['Year'].astype(str)

#combining data fields
data['Date'] = data['Day'] + "-" + data['Month'] + "-" + data["Year"]

#using iloc to view specific columns/rows
data.iloc[0] #view row with the index 0
data.iloc[0:3] #view first three rows
data.iloc[:-5] #view last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows of column 3 as index starts from 0

data.iloc[4,2] #brings in the 5th row of 3 column as row and column index starts from 0

#using split to split the clientkeywords field
split_col = data['ClientKeywords'].str.split(',', expand = True)

data['ClientAge'], data['ClientType'], data['LengthofContract'] = split_col[0], split_col[1], split_col[2]

#using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using lower function to change Item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset
new_data = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merge files on key = month
data = pd.merge(data, new_data, on = "Month")

#drop columns
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Month', axis = 1)
data = data.drop('Year', axis = 1)

#export into a csv
data.to_csv('ValueInc_cleaned.csv', index = False)
