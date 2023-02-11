# ---------------------------------------- BIBLIOTECAS -----------------------------------------------------------------

import streamlit as st
import pandas as pd

# ----------------------------------------------- CARREGAMENTO DOS DADOS -----------------------------------------------

st.set_page_config(layout='wide')

dataframe_macys = pd.read_csv('data/vitrine_macys.csv')
dataframe_hm = pd.read_csv('data/vitrine_hm.csv')


# ------------------------------------------------ TRANSFORMAÇÃO DOS DADOS ---------------------------------------------


@st.cache_data()
def metrics_hm(dataframe):

    # Cálculo da Métricas
    dataframe_auxiliar = (dataframe[['fit', 'product_price']].groupby('fit')
                                                             .agg(['max', 'min', 'mean', 'median']).reset_index())

    # Separação dos DataFrames
    df_prices = dataframe_auxiliar['product_price']
    df_name_models = pd.DataFrame(dataframe_auxiliar['fit'])

    # Concatenação dos Dados
    metricas_hm = pd.concat([df_name_models, df_prices], axis=1)

    return metricas_hm


@st.cache_data()
def metrics_macys(dataframe):

    # Cálculo da Métricas
    dataframe_auxiliar = (dataframe[['fit', 'price']].groupby('fit')
                          .agg(['max', 'min', 'mean', 'median']).reset_index())

    # Separação dos DataFrames
    df_prices = dataframe_auxiliar['price']
    df_name_models = pd.DataFrame(dataframe_auxiliar['fit'])

    # Concatenação dos Dados
    metricas_macys = pd.concat([df_name_models, df_prices], axis=1)

    return metricas_macys


def visualizacao_dados_metrics(dataset):

    filter_attibutes = st.multiselect('Selecionar Colunas', dataset.columns)

    if filter_attibutes:
        df = dataset.loc[:, filter_attibutes]
    else:
        df = dataset.copy()

    return st.dataframe(df)


# --------------------------------------------- CÓDIGO PRINCIPAL -------------------------------------------------------


with st.sidebar:

    st.image('images/logo_sidebar.jpg')
    page = st.selectbox("Navegue pelo Projeto", ["Apresentação", "Vitrine H&M",
                                                 "Vitrine Macys", "Respondendo as Perguntas do CEO"])


# , "Comparação Macys x H&M", "Respondendo as Perguntas do CEO"

# --------------------------------------------- APRESENTAÇÃO -----------------------------------------------------------


if page == 'Apresentação':

    #  Apresentação
    st.title('LOJA DE E-COMMERCE STARJEANS! STORE')

    st.image('images/imagem_fundo_apresentacao.jpg')

    st.write('Seja bem-vindo ao Dashboard da StarJeans! Store. Aqui você encontrará o desenvolvimento de um projeto de '
             'consultoria para a e-commerce de moda masculida StarJeans! Store. Nesse projeto, o objetivo é ajudar os '
             'CEOs da empresa a escolherem os produtos, as matérias-primas, os modelos e as estipulações de preço das '
             'calças masculinas baseado na concorrência. Para isso, vamos entender um pouco o modelo de negócio dessa '
             'empresa.')

    st.subheader('MODELO DE NEGÓCIO')

    st.write('Eduardo e Marcelo são dois brassieres, amigos e sócios de empreendimento. Depois de vários '
             'negócios bem sucedidos, eles estão planejando se lançar no mercado de moda dos USA como um '
             'modelo de negócio do tipo E-commerce. A idéia inicial é entrar no mercado com apenas um produto e para '
             'um público específico, no caso, o produto seria calças Jeans para o público masculino. O objetivo é '
             'manter o custo de operação baixo e escalar a medida que forem conseguindo clientes')
    st.write('Porém, mesmo com o produto de entrada e a audiência definidos, os dois sócios não tem experiência '
             'nesse mercado de moda e, portanto, não sabem definir coisas básicas como preço, o tipo de calça e o '
             'material para a fabricação de cada peça. Assim, os dois sócios contrataram uma consultoria de um '
             'Cientista de Dados(no caso, eu) para nessa empreitada.')

    st.subheader('QUESTÕES DE NEGÓCIO')

    st.write('Nessa consultoria, os CEOs esperam que eu responda as seguintes questões de negócio: ')

    st.write('1. Qual o melhor preço de venda para as calças?')

    st.write('2. Quantos tipos de calças e suas cores para o produto inicial?')

    st.write('3. Quais as matérias-prima necessárias para confeccionar as calças?')

    st.write('Além dessas questões, foi nos informado que as principais concorrentes da empresa Start Jeans! serão '
             'as americanas H&M e Macys.')

    st.subheader('TOMADA DE DECISÃO PARA A RESOLUÇÃO DO PROBLEMA NEGÓCIO')

    st.write('Com a informação de que as principais concorrentes da StarJeans! Store serão a H&M e a Macys, a tomada '
             'de decisão para resolver esse problema foi o desenvolvimento de foi scripts em python para a extração de '
             'dados das webpages da H&M e Macys com o objetivo de extrair dados relevantes sobre modelo de calças, '
             'materiais que compõem as calças, preços e outras informações relevantes')

    st.subheader('CONCLUSÃO')

    st.write('O objetivo do projeto foi concluído com sucesso. Foi extraído informações extremamente relevantes sobre '
             'preços, matéria-primas para produção, modelo de calças, distribuição de preços e comparação de preços '
             'entre as concorrências. Para ter acesso a todas essas informações, basta navegar pelo projeto na barra '
             'lateral a esquerda.')


# --------------------------------------------- VITRINE H&M -----------------------------------------------------------


elif page == 'Vitrine H&M':

    # Título
    st.title('VITRINE DE PRODUTOS H&M')

    # Exibição da logo
    st.image('images/logotipo_hm.jpg')

    st.write('Nessa seção, veremos todas informações extraídas da webpage da H&M. Na tabela abaixo, temos as '
             'informações detalhadas sobre cada produto extraído. Além disso, logo após, temos uma análise de preços '
             'de mercado das calças masculinas vendidas pela H&M')

    st.subheader('TABELA DE PRODUTOS')

    # Visualização dos dados
    visualizacao_dados_metrics(dataframe_hm)

    st.subheader('ANÁLISE DE PREÇOS DE MERCADO DAS CALÇAS JEANS DA H&M')

    st.subheader('Preço Máximo das Calças')
    st.image('images/preco_maximo_calcas_hm.png')

    st.subheader('Preço Mínimo das Calças')
    st.image('images/preco_minimo_calcas_hm.png')

    st.subheader('Preço Médio das Calças')
    st.image('images/preco_medio_calcas_hm.png')

    st.subheader('Distribuição dos Preços das Calças')
    st.image('images/distribuicao_precos_calcas_hm.png')

# ------------------------------------------------------- VITRINE MACYS ------------------------------------------------

elif page == 'Vitrine Macys':

    # Título
    st.title('VITRINE DE PRODUTOS MACYS')

    # Exibição da logo
    st.image('images/logotipo_macys.png')

    st.write('Nessa seção, veremos todas informações extraídas da webpage da Macys. Na tabela abaixo, temos as '
             'informações detalhadas sobre cada produto extraído. Além disso, logo após, temos uma análise de preços '
             'de mercado das calças masculinas vendidas pela Macys')

    st.subheader('TABELA DE PRODUTOS')

    # Visualização dos dados
    visualizacao_dados_metrics(dataframe_macys)

    st.subheader('ANÁLISE DE PREÇOS DE MERCADO DAS CALÇAS JEANS DA H&M')

    st.subheader('Preço Máximo das Calças')
    st.image('images/preco_maximo_calcas_macys.png')

    st.subheader('Preço Mínimo das Calças')
    st.image('images/preco_minimo_calcas_macys.png')

    st.subheader('Preço Médio das Calças')
    st.image('images/preco_medio_calcas_macys.png')

    st.subheader('Distribuição dos Preços das Calças')
    st.image('images/distribuicao_precos_calcas_macys.png')


elif page == "Respondendo as Perguntas do CEO":

    st.subheader('1. Qual o melhor preço de venda para as calças?')

    st.write('Logo abaixo temos os preços lado a lado para os CEOs tomarem a melhor decisão.')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Preço Máximo H&M')
        st.image('images/preco_maximo_calcas_hm.png')

    with col2:
        st.subheader('Preço Máximo Macys')
        st.image('images/preco_maximo_calcas_macys.png')

    col3, col4 = st.columns(2)

    with col3:
        st.subheader('Preço Médio H&M')
        st.image('images/preco_medio_calcas_hm.png')

    with col4:
        st.subheader('Preço Medio Macys')
        st.image('images/preco_medio_calcas_macys.png')

    col5, col6 = st.columns(2)

    with col5:
        st.subheader('Preço Mínimo H&M')
        st.image('images/preco_minimo_calcas_hm.png')

    with col6:
        st.subheader('Preço Mínimo Macys')
        st.image('images/preco_minimo_calcas_macys.png')

    st.subheader('2. Quantos tipos de calças e suas cores para o produto inicial?')

    st.write('Logo abaixo temos os catálogo de todos os tipos de calças, seus modelos, suas cores e suas combinações '
             'possíveis.')
    st.write('Analisando o catálogo da H&M nós temos {} modelos de calças e {} cores diferentes.Dessa forma, nós temos '
             'para o produto inicial {} possibilidades só com o '
             'catálogo da H&M.'.format(len(dataframe_hm['fit'].unique()),
                                       len(dataframe_hm['color_name'].unique()),
                                       len(dataframe_hm['fit'].unique())*len(dataframe_hm['color_name'].unique())))

    st.write('Analisando o catálogo da Macys nós temos {} modelos de calças e {} cores diferentes. Dessa forma, nós '
             'temos para o produto inicial {} possibilidades só com o catálogo da '
             'Macys.'.format(len(dataframe_macys['fit'].unique()),
                             len(dataframe_macys['color'].unique()),
                             len(dataframe_macys['fit'].unique()) * len(dataframe_macys['color'].unique())))

    col1, col2 = st.columns(2)

    with col1:
        vitrine_hm = dataframe_hm[['product_name', 'color_name', 'fit', 'size_number']]
        st.subheader('Catalogo H&M')
        st.write('Na tabela abaixo podemos ver as calças e cores.')
        st.dataframe(vitrine_hm)

    with col2:
        vitrine_macys = dataframe_macys[['product_name', 'color', 'fit', 'size']].copy()
        st.subheader('Catálogo Macys')
        st.write('Logo abaixo, podemos ver as calças, as cores e tamanhos.')

        st.dataframe(vitrine_macys)

    st.subheader('3. Quais as matérias prima necessárias para confeccionar as calças?')

    st.write('As principais materiais-primas usadas pela H&M para a confecção de calças é o algodão, o poliester e o '
             'spandex. Já, a Macys, utiliza algodão, polyester, spandex, viscose, lyocell e elastano.')
    st.write('Portanto, a sugestão é de que, inicialmente, as calças tenham na sua composição três matérias-primas '
             'que são o algodão, poliester e spandex.')

# ----------------------------------------------------------------------------------------------------------------------
