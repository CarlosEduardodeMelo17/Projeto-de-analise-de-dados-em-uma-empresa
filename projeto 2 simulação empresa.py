#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from math import ceil

#cria o objeto calculator 
class Calculator():
    #metodo construtor que armazena em sales o dataframe
    def __init__(self, data_values):
        self.sales = data_values
    
    #metodo que soma os valores 
    def Sum(self):
        total_sales = self.sales.sum()
        print(f'O valor total arrecadado por cadaproduto é de: \n{total_sales}')
        
    #método para média
    def Mean(self):
        month_mean = self.sales.mean()
        print(f'A média mensal de cada produto é de: \n{month_mean}')
        
    #método para maior valor
    def M_index(self):
        max_i = self.sales.idxmax()
        print(f'O valor de vendas mensais com maior valor são: \n{max_i}')
        
    def T_vendas(self):
        trimestres = df.resample('Q').sum()
        print(f"Total de Vendas por Trimestre: \n{trimestres}")
        

#cria o Data Frame apartir da dict data
data = {
    'Data': pd.date_range(start = '2023-01-01', end = '2023-12-31', freq = 'M'),
    'Produto_A': np.random.randint(100, 500, size = 12),
    'Produto_B': np.random.randint(50, 800, size = 12),
    'Produto_C': np.random.randint(300, 700, size = 12)
} 
df = pd.DataFrame(data)
df.set_index('Data', inplace=True)
df.head(12)

#gera o objeto cal que soma o total de vendas de cada produto ao londo do ano
cal = Calculator(df)

#método Sum que calcula a soma total
cal.Sum()

print()

#método que calcula a média mensal
cal.Mean()

print()

#método que procura o més com maior valor de venda
cal.M_index()

print()
#método que procura total de vendas por trimestre
cal.T_vendas()


# In[34]:


date = pd.date_range(start = '2023-01-01', end = '2023-12-31', freq = 'M')
date

