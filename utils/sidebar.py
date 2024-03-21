# Bibliotecas Padrão
import streamlit as st

from streamlit_option_menu import option_menu

# Recursos Locais
import utils.style as utSt

from utils.dataset import df


def menu_sidebar():
    app = option_menu(
        menu_title="Jogos Eletrônicos",
        options=['Home', 'Operacional', 'Tático', 'Estratégico',
                 'Analítico', 'Outros', 'Sobre'],
        icons=[],
        menu_icon='controller',
        default_index=0,
        styles=utSt.estilo_menu
    )

    if app == 'Home' or app == 'Sobre':
        anos_selecionados = df
        genero_selecionados = df
        desenvolvedora_selecionados = df

    else:
        # -------------Filtrar Ano-------------#
        anos = sorted(df['Year'].unique())
        anos_selecionados = st.multiselect(
            'Anos:', anos, placeholder='Selecione...')

        # -------------Filtrar Gênero-------------#
        genero = sorted(df['Genre'].unique())
        genero_selecionados = st.multiselect(
            'Gênero:', genero, placeholder='Selecione...')

        # -------------Filtrar Desenvolvedora-------------#
        desenvolvedora = sorted(df['Publisher'].unique())
        desenvolvedora_selecionados = st.multiselect(
            'Desenvolvedora:', desenvolvedora, placeholder='Selecione...')

    return app, anos_selecionados, genero_selecionados, desenvolvedora_selecionados
