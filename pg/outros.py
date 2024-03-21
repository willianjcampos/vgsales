import streamlit as st
import altair as alt
import pandas as pd


def app(df):
    st.title('Outros')
    # Gráfico Scatter
    x2 = df.groupby(['Platform'])['Platform'].count().index
    y2 = df.groupby(['Platform'])['Platform'].count()

    grafico2 = pd.DataFrame({'Plataformas': x2,
                             'Quantidade': y2})

    st.write(alt.Chart(grafico2,
                       title=alt.Title(
                           "Lançamento por Plataformas",
                           subtitle="Plataformas que mais lançaram jogos"
                       ),
                       width="container"
                       ).mark_circle().encode(
        x=alt.X('Plataformas', sort=None),
        y='Quantidade',
    ).interactive())
