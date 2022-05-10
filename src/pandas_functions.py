import pandas as pd
import numpy as np
from nltk.probability import FreqDist
from documentParser import doc_preparer

def dataFrame_info(df):
    '''
    More verbose version of df.info()
    Displayed as a pandas dataframe
    
    Author: Saad Saeed
    '''
    print(f'Datframe has {df.shape[0]} rows and {df.shape[1]} columns')
    df_info_dict = {}
    for col in df.columns:
        
        #Don't know how to handle a column of lists yet
        if df[col].dtype == 'O':
            pass
        
        num_zeroes = (df[col] == 0).sum()
        num_nulls = df[col].isna().sum()
        num_uniques = len(df[col].unique())

        mean = 0
        median = 0

        list_missingOrUnknown = ['unknown', ' ', '', 'missing']

        try:
            num_missingOrUnknown = (df[col].map(
                lambda x: x.lower() in list_missingOrUnknown).sum())
        except:
            num_missingOrUnknown = 0

        try:
            mean = df[col].mean()
            median = df[col].median()
        except:
            mean = 0
            median = 0

        df_info_dict[col] = {'Zeroes': num_zeroes,
                             'Nulls': num_nulls,
                             'Uniques': num_uniques,
                             'Missing/Unknown': num_missingOrUnknown,
                             'Mean': mean,
                             'Median': median}
    df_pd = pd.DataFrame(
              index=pd.Index(df.columns, name='Columns:'),
              columns=pd.MultiIndex.from_product([['Zeroes', 'Nulls', 'Uniques','Missing/Unknown'],['Count', 'Fraction']], 
                                                 names=['Info Table:', 'Details:']))
    df_pd[['Mean','Median']] = np.nan

    for col, info in df_info_dict.items():
        df_pd.loc[col,('Zeroes','Count')] = info['Zeroes']
        df_pd.loc[col,('Zeroes','Fraction')] = "{:.2f} %".format((info['Zeroes'] / df.shape[0]) * 100)
        
        df_pd.loc[col,('Nulls','Count')] = info['Nulls']
        df_pd.loc[col,('Nulls','Fraction')] = "{:.2f} %".format((info['Nulls'] / df.shape[0]) * 100)
        
        df_pd.loc[col,('Uniques','Count')] = info['Uniques']
        df_pd.loc[col,('Uniques','Fraction')] = "{:.2f} %".format((info['Uniques'] / df.shape[0]) * 100)
        
        df_pd.loc[col,('Missing/Unknown','Count')] = info['Missing/Unknown']
        df_pd.loc[col,('Missing/Unknown','Fraction')] = "{:.2f} %".format((info['Missing/Unknown'] / df.shape[0]) * 100)
        
        df_pd.loc[col,'Mean'] = info['Mean']
        df_pd.loc[col,'Median'] = info['Median']
        
            
    display(df_pd)
    
    
def getTopWordFreq(df,col,n):
    '''
    generates FreqDist and prints out top n words
    df: dataframe
    col: column you want to run a freqDist on
    n: number of most common items    
    '''
    word_freq = FreqDist()
    for text in df[col].map(lambda x:doc_preparer(x,stem=False)):
        for word in text.split():
            word_freq[word] +=1
    return word_freq.most_common(n=n)
