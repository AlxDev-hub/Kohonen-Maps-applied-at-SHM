#Bibliotecas utilizadas
import pandas as pd
import numpy as np

#Leitura do banco de dados
pzt = pd.read_excel('pzt2.xlsx', header=None)

#Remoção da primeira coluna
pzt = pzt.drop(columns=[0], axis=1)

#Conversão para o formato numpy
pzt = np.array(pzt)

#Fazendo a transposta
pzt = pzt.T

#Conversão para o formato pandas
transpostaPZT = pd.DataFrame(data = pzt)

#Salvando em um arquivo .csv
transpostaPZT.to_csv('PZT2_TRANSPOSTA.csv', encoding='utf-8', index=False)
