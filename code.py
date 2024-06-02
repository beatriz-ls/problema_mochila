# Libs

import numpy as np
import pandas as pd
import random
from functools import partial

# Função objetivo
def f_objetivo(df):
    valor_total = df['Valor'].sum() # Valor total do gene do indivíduo
    peso_total = df['Peso'].sum() # Peso total do gene do indivíduo  
    return valor_total, peso_total
  
# Gerar gene do indivíduo aleatório
def f_aleatorio(df):
    n_aleatorio = np.random.randint(1, df.shape[0]+1) # Quantidade dos genes a serem escolhidos
    df_aleatorio = df.sample(n = n_aleatorio) # Gera o gene do individuo 
    return df_aleatorio

# Função aptidão
def f_aptidao(df_gene, capacidade): 
    valor = f_objetivo(df_gene)[0] # Valor total do indivíduo
    peso = f_objetivo(df_gene)[1] # Peso total do individuo

    # Ponderação que avalia se a escolha atende a capacidade máxima ou não
    if peso <= capacidade:
        podenracao = 1 # Se a escolha dos itens pesa igual ou menos que 15, o valor será 1
    else:
        podenracao = 0 # Se a escolha dos itens pesa mais que 15, o valor será 0

    aptidao = podenracao*(valor + peso) # Quanto maior o resultado, mais apto ele será 
    # Aptidão: maximar o valor e verifica se o peso atende capacidade máxima 
    return aptidao
