'''
Module for the implementation of the Partner Selection algorithms.

'''
#import needed packages
import pandas as pd
import numpy as np
import spicy as sp
class PartnersSelection:
    '''Class that contains algorithms that are used in partners selection.
    '''
    def __init__(self):
        pass
    def get_corr_matrix(self, returns_df ):
        '''Get the Spearman's correlation matrix from the returns matrix.

        parameters:(pandas df) returns_df
        returns: (pandas df) df_corr
        '''
        df_corr = returns_df.corr("spearman", min_periods=1)
        return df_corr
    def employ_trad_approach(self,df_corr):


        df_corr = df_corr.fillna(0)
        df_corr = df_corr.set_index(keys=df_corr.columns)
        df_corr_max = pd.DataFrame(df_corr.columns.values[np.argsort(-df_corr.values, axis=1)[:, :4]],
                                   index=df_corr.index,
                                   columns=['Self_Ticker', '1st Max', '2nd Max', '3rd Max'])
        df_corr_max.drop('Self_Ticker', axis=1, inplace=True)
        df_corr_sort = df_corr.apply(lambda x: np.sort(x), axis=1, raw=True)
        df_corr_sort = df_corr_sort.iloc[:, -4:]
        df_corr_sort = df_corr_sort.iloc[:, :-1]
        df_corr_sort.loc[:, "Sum"] = df_corr_sort.sum(axis=1)
        target_stock = df_corr_sort["Sum"].idxmax(axis=0)
        partners = df_corr_max.loc[target_stock].tolist()
        return (target_stock, partners)








