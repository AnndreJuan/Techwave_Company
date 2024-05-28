import streamlit as st
from PIL import Image

# 1. Configurando página inicial
st.set_page_config(page_title="Home", layout='wide')

# 2. Adicionando logo
image = Image.open('Techwave.png')
st.sidebar.image(image, width=250)

# 3. Adicionando criador
st.sidebar.markdown('#### Create by Anndre Juan')

st.write('# Techwave Company Dashboard')

st.markdown("""

## Visão de Clientes:
    Tempo Médio de Entrega: Tempo médio de entrega para cada método de entrega (Courier vs. Drone).
    Impacto das Condições Climáticas e Tráfego: Analisar como diferentes condições climáticas e densidades de tráfego afetam os tempos de entrega.
    Frequência de Entregas: Quantidade de entregas feitas por cada método em diferentes condições.

## Visão de Produtos:
    Distribuição de Categorias de Produtos: Frequência de vendas para cada categoria de produto.
    Avaliações de Produtos: Média das avaliações dos clientes para cada categoria de produto.
    Tempo Médio de Entrega por Categoria de Produto: Comparação dos tempos de entrega para diferentes categorias de produtos.
## Visão da Diretoria:
    Resumo de Vendas: Total de vendas por categoria de produto.
    Desempenho das Promoções: Comparação do impacto das promoções nas vendas e nas avaliações dos clientes.
    Análise Geográfica: Distribuição das vendas por tipo de cidade (Metropolitan, Urban).

### Entre outros insights 😎
            
#### Ask for Help - @AnndreJuan
""")