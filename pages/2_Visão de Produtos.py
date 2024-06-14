#========================================================
# VISÃO - ENTREGADORES
#========================================================

#========================================================
# Bibliotecas necessárias
#========================================================

import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

#========================================================
# Importando dataframe
#========================================================
df1 = pd.read_csv(r'dataset/techwave.csv', sep=',')
df = df1.copy()

#========================================================
# Função para limpar dataframe
#========================================================
def clear_data(df):

    df1 = df.astype(str)                                                         # Transformando dataframe em string
    df = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)          # Removendo espaços de todo o datagrame

    # Convertendo colunas para int
    df['Nota'] = df['Nota'].astype( int )
    df['Quantidade'] = df['Quantidade'].astype( int )

    # Convertendo colunas para float
    df['Preco'] = df['Preco'].astype( float )
    df['Desconto'] = df['Desconto'].astype( float )

    # Convertendo de texto para data
    # df['DataCompra'] = pd.to_datetime(df['DataCompra'], format="%d/%m/%Y")

    return df

#========================================================
# Limpando dataframe
#========================================================
clear_data(df)

#========================================================
# Funções de análises de dados
#========================================================

# METRICAS
# 1. Maior e Menor idade
def Idade(df):
    maiorIdade = df['Idade'].max()
    menorIdade = df['Idade'].min()
    col1.metric('Maior Idade', maiorIdade)
    col2.metric('Menor Idade', menorIdade)
    
# 2. Maior e Menor nota
def Nota(df):
    maiorNota = df['Nota'].max()
    menorNota = df['Nota'].min()
    col3.metric('Maior Nota', maiorNota)
    col4.metric('Menor Nota', menorNota)
    
# 3. Quantidade de Produtos → grafico de coluna
def QauntidadeProdColumn(df):
    a = df['Produto'].value_counts().reset_index()
    a.rename(columns={'count':'Quantidade'}, inplace=True)
    fig = px.bar(data_frame=a, x='Produto', y='Quantidade')
    col1.plotly_chart(fig)

# # 3. Produtos por cidade
# def produtosPorCidade(df):
#     a = df.groupby(['Product_Subcategory', 'City']).size().reset_index(name='Count')
#     fig = px.sunburst(a, path=['Product_Subcategory', 'City'], values='Count',
#                       title='Distribuição de Subcategorias de Produtos por Cidade',
#                       color_continuous_scale=px.colors.qualitative.Plotly)

#     col2.plotly_chart(fig)



#======================================================================================================================
# Layout Streamlit
#======================================================================================================================
st.markdown('### PRODUTOS')
st.markdown("---")
st.markdown('### Métricas')

with st.container():
    col1, col2, col3, col4 = st.columns(4, gap='large')

    with col1, col2:
        Idade(df)
    
    with col3, col4:
        Nota(df)

    st.markdown("---")
    st.markdown("### Avaliações")

    with st.container():
        col1, col2  = st.columns(2, gap='large')

        with col1:
            QauntidadeProdColumn(df)

        with col2:
            QauntidadeProdColumn(df)
        
    
