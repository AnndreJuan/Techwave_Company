#========================================================
# VISÃO - ENTREGADORES
#========================================================

#========================================================
# Bibliotecas necessárias
#========================================================

import pandas as pd
import plotly.express as px
import streamlit as st






#========================================================
# Importando dataframe
#========================================================
df1 = pd.read_csv(r'dataset/techwave.csv')
df = df1.copy()

#========================================================
# Função para limpar dataframe
#========================================================
def clear_data(df):

    df1 = df.astype(str)                                                         # Transformando dataframe em string
    df = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)          # Removendo espaços de todo o datagrame

    # Removendo palavra '(min)' de Time_taken(min)
    df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x: x.replace(' (min)','') if isinstance(x, str) and ' (min)' in x else x)

    # Convertendo colunas para int
    df['Customer_Age'] = df['Customer_Age'].astype(int)
    df['Time_taken(min)'] = df['Time_taken(min)'].astype(int)
    df['Multiple_orders'] = df['Multiple_orders'].astype(int)

    # Convertendo colunas para float
    df['Customer_Ratings'] = df['Customer_Ratings'].astype(float)

    # Convertendo de texto para data
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d-%m-%Y')

    print(df)
    print(df['Order_Date'].head(10))
    return df

#========================================================
# Limpando dataframe
#========================================================
clear_data(df)

#========================================================
# Funções de análises de dados
#========================================================

# 1. Idade
def idade(df):
    maiorIdade = df.loc[:, 'Customer_Age'].max()
    menorIdade = df.loc[:, 'Customer_Age'].min()
    col1.metric('Maior Idade', maiorIdade)
    col2.metric('Menor Idade', menorIdade)

# 2. Avaliação média por cliente
def avaliacoes(df):
    melhorAvaliacao = df.loc[:, 'Customer_Ratings'].max()
    menorAvaliacao = df.loc[:, 'Customer_Ratings'].min()
    col3.metric('Melhor avaliação', melhorAvaliacao)
    col4.metric('Pior avaliação', menorAvaliacao)
    
# 3. Avaliação média por cliente
def avaliacao_media_entregador(df, col1):
    col1.markdown('##### Avaliações Médias Por Cliente')
    d = df.loc[:, ['Customer_ID', 'Customer_Ratings']].groupby(['Customer_ID']).mean().reset_index()
    d = d.rename(columns={'Customer_ID': 'ID Cliente', 'Customer_Ratings': 'Avaliação Média'})
    d['Avaliação Média'] = d['Avaliação Média'].round(2)
    col1.dataframe(d, height=500, width=400)

#======================================================================================================================
# Layout Streamlit
#======================================================================================================================
st.markdown('### ENTREGADORES')
st.markdown("---")
st.markdown('### Métricas')
with st.container():
    col1, col2, col3, col4= st.columns(4, gap='large')
    
    # 1. Maior e Menor Idade
    with col1, col2:
        idade(df)

    # 1. Melhor e Pior Avaliação
    with col3, col4:
        avaliacoes(df)
