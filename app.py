# Bibliotecas Padrão
import pg.home as home
import pg.operacional as operacional
import pg.analitico as analitico
import pg.estrategico as estrategico
import pg.tatico as tatico
import pg.outros as outros
import pg.sobre as sobre
from utils.dataset import df
import utils.style as utSt
import utils.sidebar as utSidebar
import streamlit as st
import pandas as pd

from streamlit_option_menu import option_menu

# -------------Configuração da Página-------------#
st.set_page_config(
    page_title="Jogos Eletrônicos",
    page_icon=":video_game:",
    layout='wide'
)


# Bibliotecas Local


# -------------Para usar estilo CSS-------------#
with open(utSt.estilo_css, encoding='utf8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# -------------Classe Principal-------------#
@st.cache_data
class MainApplication:
    def __init__(self) -> None:
        self.app = []

    def run() -> None:
        # -------------Sidebar-------------#
        with st.sidebar:
            app, anos_selecionados, genero_selecionados, desenvolvedora_selecionados = utSidebar.menu_sidebar()

        # -------------Pg Home-------------#
        if app == 'Home':
            home.app()

        # -------------Pg Operacional-------------#
        if app == 'Operacional':
            operacional.app(anos_selecionados, genero_selecionados,
                            desenvolvedora_selecionados)

        # -------------Pg Analítico-------------#
        if app == 'Analítico':
            analitico.app()

        # -------------Pg Estratégico-------------#
        if app == 'Estratégico':
            estrategico.app()

        # -------------Pg Tático-------------#
        if app == 'Tático':
            tatico.app()

        # -------------Pg Outros-------------#
        if app == 'Outros':
            outros.app(df)

        # -------------Pg Informações-------------#
        if app == 'Sobre':
            sobre.app()
    run()


# def main():
#     app = MainApplication()


# if __name__ == "__main__":
#     main()
