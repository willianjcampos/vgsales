import streamlit as st
import streamlit.components.v1 as components


def app():
    st.title('Lançamento de Jogos Eletrônicos')
    st.header('Projeto de Análise de DataFrame')
    st.write('Este projeto foi criado para efetuar a avaliação relacionada ao desenvolvimento de Dashboards através de ferramentas de exibição gráfica em conjunto com o Streamlit para gerar relatórios em formato Web dinâmicos.')
    st.header('Sobre o Projeto')
    st.write('')
    st.write('')
    col1, col2 = st.columns([2, 4])
    with col1:
        st.image(r'arquivos\will.jpg', caption='Willian JC Almeida', width=250)

    with col2:
        st.header('Willian JC Almeida')
        st.markdown(
            '''Linkedin: https://br.linkedin.com/in/willianjcampos \n\n Github: https://github.com/willianjcampos''')




