import streamlit as st
from streamlit_option_menu import option_menu
import pg.home as home
import pg.analitico as analitico
import pg.tatico as tatico
import pg.estrategico as estrategico
import pg.sobre as sobre
import pandas as pd



## Configuração da Página
st.set_page_config(
    page_title="Venda de Jogos",
    page_icon="⚖️",
    layout='wide'
)


## Classe Principal
@st.cache_data
class MultiApp:
    def __init__(self) -> None:
        self.app = []


    def run():
        # Carrega a base de dados
        df = pd.read_csv(r'sempre_bem_ti/base_dados_tratada.csv', encoding='utf-8')


        # Configura Sidebar
        with st.sidebar:
            # Configuração do Menu
            app = option_menu(
                menu_title="Venda de Jogos",
                options=['Home', 'Analítico', 'Tático', 'Estratégico', 'Sobre'],
                icons=[],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    'container': {'padding': '5px !important'},
                    'icon': {'font-size': '14px'},
                    'nav-link': {'font-size': '14px',
                                 'text-align': 'left',
                                 'margin': '2px 0px',
                                 '--bs-nav-link-padding-x': '0.5rem',
                                 '--bs-nav-link-padding-y': '0.5rem'},
                    'nav-link-selected': {'font-size': '14px',
                                          'font-weight': 'normal'}
                }
            )
            anos = sorted(df['Ano'].unique())
            anos_selecionados = st.multiselect('Ano:', anos, placeholder='Selecione...')

            genero = sorted(df['Mes'].unique())
            genero_selecionados = st.multiselect('Mês:', genero, placeholder='Selecione...')

        if app == 'Home':
            home.app()
        
        if app == 'Analítico':
            analitico.app()

        if app == 'Tático':
            tatico.app()

        if app == 'Estratégico':
            estrategico.app()

        if app == 'Sobre':
            sobre.app()

    
    run()
