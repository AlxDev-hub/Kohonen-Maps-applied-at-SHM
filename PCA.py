#Bibliotecas utilizadas
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Leitura do banco de dados
PCAPZT20 = pd.read_csv('PZT2_TRANSPOSTA.csv')

#Padronização dos dados
PCAPZT20 = StandardScaler().fit_transform(PCAPZT20)

#Determinando o número de componentes
pca = PCA(n_components=20)

#Ajusta o modelo e aplica a redução de dimensionalidade
principalComponents = pca.fit_transform(PCAPZT20)

#Conversão para o formato pandas
principalDf = pd.DataFrame(data= principalComponents)

#Salvando em um arquivo .csv
principalDf.to_csv('PCA_PZT_20.csv', encoding='utf-8', index=False)
