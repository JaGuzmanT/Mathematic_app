# Loading libraries
import streamlit as st
from json import load
import base64

#----------------------------------------------------------------#
# Configuración de las páginas de la webapp
def page_configuration():
    st.set_page_config(page_title="CalcMaster",
                page_icon="Images/Logo.ico",
                layout="wide",
                initial_sidebar_state="auto")
#----------------------------------------------------------------#
# Configuración del sidebar
def sidebar_elements():
    # side_background_exten = "webp"
    # side_image = "Images/Logo_sidebar.webp"
    # st.markdown(
    #         f"""
    #         <style>
    #         [data-testid="stSidebar"] > div:first-child {{
    #         background: url(data:image/{side_background_exten};base64,{base64.b64encode(open(side_image, "rb").read()).decode()});
    #         }}
    #         </style>
    #         """,
    #         unsafe_allow_html=True
    # )
    st.sidebar.title("CalcMaster WebApp 1.0.1")

    # Defining all the pages and the interface into the sidebar
    with st.sidebar:
        st.page_link(page="Central_app.py", label="Home", icon=":material/home:" )
        st.page_link(page="pages/functions.py", label="Funciones", icon=":material/monitoring:")
        st.page_link(page="pages/limit.py", label="Límites", icon=":material/query_stats:")

        st.divider()
        st.write(":orange[Aplicación Web para cálculo universitario]")
#----------------------------------------------------------------#
# Imagen de la página de Inicio
@st.cache_resource
def imagen_inicio():
    st.image("Images/Logo_1.webp", width=500)
#----------------------------------------------------------------#
# Configuración de las animaciones
def load_lottiefile(filename: str):
                with open(file=filename, mode='r') as f:
                    return load(f)
#----------------------------------------------------------------#
# Ocultando el botón de hamburguesa y de Github
def hide_elements(hide_menu=True, hide_footer=True, hide_header=True):
    style = "<style>"
    if hide_menu:
        style += "#MainMenu {visibility: hidden;}"
    if hide_footer:
        style += "footer {visibility: hidden;}"
    if hide_header:
        style += "header {visibility: hidden;}"
    style += "</style>"
    st.markdown(style, unsafe_allow_html=True)