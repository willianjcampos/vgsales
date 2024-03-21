import streamlit as st
import pandas as pd
import locale
import altair as alt
import streamlit.components.v1 as components


import utils.style as utSt
import utils.graficos as grafico
from utils.dataset import df


bloco_estilo = f'''<style>{utSt.estilo_bloco}</style>'''


def cols_primeira_linha(df):
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        ns_sales_total = locale.format('%.2f', df['NA_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>NA</h1>
                <p>{ns_sales_total}</p>
            """
        )

    with col2:
        eu_sales_total = locale.format('%.2f', df['EU_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>EU</h1>
                <p>{eu_sales_total}</p>
            """
        )

    with col3:
        jp_sales_total = locale.format('%.2f', df['JP_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>JP</h1>
                <p>{jp_sales_total}</p>
            """
        )

    with col4:
        other_sales_total = locale.format(
            '%.2f', df['Other_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>OUTROS</h1>
                <p>{other_sales_total}</p>
            """
        )

    with col5:
        global_sales_total = locale.format(
            '%.2f', df['Global_Sales'].sum(), True)

        components.html(
            f"""
                <body style='background-color: blue;'>
                {bloco_estilo}
                <h1>TOTAL</h1>
                <p>{global_sales_total}</p>
                </body>
            """
        )


def cols_segunda_linha(eixo_x, eixo_y, df_genero):
    col1, col2 = st.columns([3, 2])

    # Gráfico de Linhas
    with col1:
        aba1, aba2 = st.tabs(['Linha', 'Coluna'])
        with aba1:
            grafico.volume_jogos_ano_linha(eixo_x, eixo_y)

        with aba2:
            grafico.volume_jogos_ano_coluna(eixo_x, eixo_y)

    # Gráfico de Pizza
    with col2:
        aba21, aba22 = st.tabs(['Setor', 'Coluna'])
        with aba21:
            grafico.volume_jogos_genero_setor(df_genero)
        
        with aba22:
            grafico.volume_jogos_genero_barra_h(df_genero)


def cols_terceira_linha(eixo_x, eixo_y):
    col1, col2 = st.columns([1, 5])

    # Rank
    with col1:
        contagem = 3
        if len(eixo_x) >= contagem:
            for i in range(contagem):
                p = i + 1
                titulo = str('%iº' % p)
                valor = str(eixo_x[i] + " - " + locale.format('%d', eixo_y[i], True))
                components.html(f"""
                                {bloco_estilo}
                                <h1>{titulo}</h1>
                                <p>{valor}</p>
                                """)

        elif len(eixo_x) >= 1:
            titulo = "1º"
            valor = str(eixo_x[0] + " - " + locale.format('%d', eixo_y[0], True))
            components.html(f"""
                                {bloco_estilo}
                                <h1>{titulo}</h1>
                                <p>{valor}</p>
                                """)

        else:
            st.write('Dados indisponíveis')

    # Gráfico de Barras
    with col2:
        grafico = pd.DataFrame({'Plataformas': eixo_x[0:10],
                                'Quantidade': eixo_y[0:10]})

        st.write(alt.Chart(grafico,
                           title=alt.Title(
                               "Plataformas",
                               subtitle="As 10 Plataformas que mais reuniram recursos"
                           ),
                           width="container"
                           ).mark_bar(color='#FF4B4B').encode(
            x=alt.X('Plataformas', sort=None),
            y='Quantidade'
        ).interactive())




def app(anos_selecionados, genero_selecionados, desenvolvedora_selecionados):
    # Cria as variáveis de filtros
    df_ano = df[df['Year'].isin(anos_selecionados)]
    df_genero = df[df['Genre'].isin(genero_selecionados)]
    df_desenvolvedora = df[df['Genre'].isin(desenvolvedora_selecionados)]


    # PRIMEIRA LINHA
    # Verifica Filtro de Período (Anos) de Venda
    if df_ano.shape[0] > 0:
        cols_primeira_linha(df_ano)

    else:
        cols_primeira_linha(df)

    # SEGUNDA LINHA
    # Verifica Filtro de Gênero de Jogos
    if df_genero.shape[0] > 0:
        eixo_x = df_genero.groupby(['Year'])['Year'].count().index
        eixo_y = df_genero.groupby(['Year'])['Year'].count()
        cols_segunda_linha(eixo_x, eixo_y, df_genero)

    else:
        eixo_x = df.groupby(['Year'])['Year'].count().index
        eixo_y = df.groupby(['Year'])['Year'].count()
        cols_segunda_linha(eixo_x, eixo_y, df)

    # TERCEIRA LINHA
    if df_genero.shape[0] > 0:
        eixo_x = df_genero.groupby(['Platform'])[
            'Platform'].count().sort_values(ascending=False).index
        eixo_y = df_genero.groupby(['Platform'])[
            'Platform'].count().sort_values(ascending=False)

    else:
        eixo_x = df.groupby(['Platform'])['Platform'].count(
        ).sort_values(ascending=False).index
        eixo_y = df.groupby(['Platform'])[
            'Platform'].count().sort_values(ascending=False)

    cols_terceira_linha(eixo_x, eixo_y)
