# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:45:28 2023

@author: 91998
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel file
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#counting the no of articles per source
data.groupby(['source_id'])['article_id'].count()

#no of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping engagement_comment_plugin_count as we will not be using it
data.drop('engagement_comment_plugin_count', axis = 1, inplace = True)

#creating a keyword flag
def keywordflag(keyword):
    length = len(data)
    print(type(length))
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
    
keywordflag = keywordflag("crash")

#creating a new column 
data['keyword_flag'] = pd.Series(keywordflag)

#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = data['title'][15]
analyze = sent_int.polarity_scores(text)

#adding for loop to extract sentiment for each title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#writing data 
data.to_excel('blogme_clean.xlsx', sheet_name = "blogmedata", index = False)
