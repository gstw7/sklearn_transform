from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    
   

def subs_notas(df, columns, nota, subs):
    
    '''df: Dataframe
    columns: Coluna que irá se verificada
    nota: limite da nota
    subs: nota para o qual quem está acima do limite irá ser substituida'''
    
    df.loc[df[columns] > nota, columns] = subs
    return df
