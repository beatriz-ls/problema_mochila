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
  
# Realiza o crossover
def f_crossover(df_pai_1, df_pai_2): # Crossover do pai 1 (df_x) e pai 2 (df_y)
    df_gene_pai_1_aleatorio = f_aleatorio(df_pai_1) # Coleta uma parte do gene do pai 1
    df_gene_pai_2_aleatorio = f_aleatorio(df_pai_2) # Coleta uma parte do gene do pai 2
    df_concat = pd.concat([df_gene_pai_1_aleatorio, df_gene_pai_2_aleatorio]) # Concatena as partes dos pais
    df_gene_filho = df_concat.drop_duplicates() # Remove-se linhas duplicadas
    return df_gene_filho # Retorna o filho

# Realiza a mutação
def f_mutacao(df_gene, df_mochileiro):
    linha = np.random.randint(0, df_gene.shape[0]) # Seleciona-se a linha que sofrerá mutação, somente uma única linha que será mutada
    mutacao = df_mochileiro.sample(n = 1) # Seleciona-se o gene mutação
    df_gene.iloc[linha] = mutacao # Realiza-se a mutação
    df_gene = df_gene.drop_duplicates() # Remove-se duplicadas ??????????????? criar função pra selecionar a mutacao que nao esteja no df a ser mutacionado
    return df_gene
  
# Algoritmo genético
def algoritmo_genetico(df_mochileiro, capacidade):
    # Gera a população inicial
    populacao = [f_aleatorio(df_mochileiro) for _ in range(50)] # n números da população inicial
    
    for _ in range(100):  # n números de gerações
        # Avalia a aptidão da população
        aptidao_populacao = [f_aptidao(df_gene = x, capacidade = capacidade) for x in populacao] # Calcula a aptidão de cada seleção de itens na população atual

        # Seleciona os pais por torneio
        parentes = random.choices(populacao, weights = aptidao_populacao, k = 100) # A função random.choices é usada para selecionar aleatoriamente 20 pais da população atual. A probabilidade de um indivíduo ser escolhido como pai é proporcional à sua aptidão. Isso significa que os indivíduos com maior aptidão têm uma maior probabilidade de serem escolhidos como pais.
        
        # Gera a próxima geração por crossover e mutação
        nova_geracao = [f_mutacao(df_gene = f_crossover(random.choice(parentes), random.choice(parentes)), df_mochileiro = df_mochileiro) for _ in range(50)]

        # Substitui a população atual pela próxima geração
        populacao = nova_geracao
    

    f_aptidao_fixando_capacidade = partial(f_aptidao, capacidade = capacidade) # Fixa-se  a capacidade da função apitdão
    resultado = max(populacao, key = f_aptidao_fixando_capacidade) # Implementa na última geração

    # Retorna o melhor indivíduo da última geração
    return resultado
  
# Aplicação

# Dados dos itens, valores e peso
dado = {'Item': [1, 2, 3, 4, 5],
        'Valor': [4, 2, 1, 2, 10],
        'Peso': [12, 2, 1, 1, 4]}
 
# Criando data frame
df = pd.DataFrame(dado)

# Atribuição do peso máximo a ser carregado na mochila
capacidade_max = 15

resultado = algoritmo_genetico(df_mochileiro = df, capacidade = capacidade_max)
print(resultado)
