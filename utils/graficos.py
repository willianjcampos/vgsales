import altair as alt
import seaborn as sns
import plotly.express as px
import pandas as pd
import streamlit as st

from utils.dataset import df


def volume_jogos_ano_linha(eixo_x, eixo_y, estilo='altair'):
    titulo = 'Volume de Jogos'
    subtitulo = 'Volume de Jogos desenvolvidos ao longo dos anos'

    if estilo == 'altair':
        grafico3 = pd.DataFrame({'Volume de Vendas de Jogos': eixo_y,
                                 'Anos': eixo_x})

        st.write(alt.Chart(grafico3,
                           title=alt.Title(titulo, subtitle=subtitulo),
                           width="container"
                           ).mark_line(point=True,
                                       color='#FF4B4B',
                                       interpolate='cardinal'
                                       ).encode(x=alt.X('Anos', sort=None),
                                                y='Volume de Vendas de Jogos',
                                                ).interactive())

    elif estilo == 'plotly':
        # Quantidade de jogos publicados por ano
        x_anos = df['Year'].drop_duplicates(
        ).sort_values(ascending=True).values
        # x_anos = df.groupby(['Ano'])['Ano'].count().index  # Outra forma de fazer a mesma ação anterior

        y_contagem = df['Year'].value_counts().sort_index().values
        # y_contagem = df.groupby(['Ano'])['Ano'].count()  # Outra forma de fazer a mesma ação anterior

        fig = px.line(x=x_anos, y=y_contagem,
                      labels={
                          "y": "Quantidade de Jogos",
                          "x": "Período"},
                      title=f'{titulo}<br><sup>{subtitulo}</sup>',
                      line_shape='spline',
                      markers=True)
        fig.update_layout(xaxis_range=[1980, 2020])


def volume_jogos_ano_coluna(eixo_x, eixo_y, estilo='altair'):
    titulo = 'Volume de Jogos'
    subtitulo = 'Volume de Jogos desenvolvidos ao longo dos anos'

    if estilo == 'altair':
        grafico3 = pd.DataFrame({'Volume de Vendas de Jogos': eixo_y,
                                 'Anos': eixo_x})

        st.write(alt.Chart(grafico3,
                           title=alt.Title(titulo, subtitle=subtitulo),
                           width="container"
                           ).mark_bar(color='#FF4B4B').encode(x=alt.X('Anos', sort=None),
                                                              y='Volume de Vendas de Jogos',
                                                              ).interactive())


def volume_jogos_genero_setor(df_genero):
    titulo = 'Jogos por Gênero'
    subtitulo = 'Volume de Jogos desenvolvidos por Gênero'

    # Filtro de dados... usar a lib df depois
    x4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(
        ascending=False).index  # Nomes (names)
    y4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(
        ascending=False)  # Quantidade (values)

    grafico4 = pd.DataFrame({'Setores': x4,
                             'Valores': y4})

    st.write(alt.Chart(grafico4,
                       title=alt.Title(titulo, subtitle=subtitulo),
                       width='container'
                       ).mark_arc(innerRadius=60).encode(
                           theta='Valores',
                           color='Setores',
                           ).interactive())


def volume_jogos_genero_barra_h(df_genero):
    titulo = 'Jogos por Gênero'
    subtitulo = 'Volume de Jogos desenvolvidos por Gênero'

    # Filtro de dados... usar a lib df depois
    x4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(
        ascending=False).index  # Nomes (names)
    y4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(
        ascending=False)  # Quantidade (values)

    grafico4 = pd.DataFrame({'Setores': x4,
                             'Valores': y4})   


    st.write(alt.Chart(grafico4,
                       title=alt.Title(titulo, subtitle=subtitulo),
                       width='container'
                       ).mark_bar(color='#FF4B4B').encode(
                           x='Valores',
                           y=alt.Y('Setores', sort=None)
                           ).interactive())