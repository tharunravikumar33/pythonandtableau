# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 09:48:41 2023

@author: 91998
"""

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform list to Dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()

#using exp() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#checking FICO score category
fico_category = []
length = len(loandata)
for x in range(0, length):
    fico = loandata['fico'][x]

    if fico >= 300 and fico < 400:
        ficocat = 'Very Poor'
    elif fico >= 400 and fico <600:
        ficocat = 'Poor'
    elif fico >= 601 and fico <660:
        ficocat = 'Fair'
    elif fico >= 660 and fico <700:
        ficocat = 'Good'
    elif fico >= 700:
        ficocat = 'Excellent'
    else:
        ficocat = 'Unknown'
    fico_category.append(ficocat)
    
#converting list to panda series
Fico_Category = pd.Series(fico_category)

#appending fico_category in to dataframe
loandata['fico_category'] = Fico_Category

#df.loc conditional statements
#for interest rate, we need a new column, rate > 0.12 then high else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#checking no of loans base on purpose and plotting them
purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'green', width = 0.1)
plt.show()

#scatter plots
xpoint = loandata['dti']
ypoint = loandata['annualincome']
plt.scatter(xpoint, ypoint)
plt.show()
 
#writing to csv
loandata.to_csv('loandata_cleaned.csv', index = True)
