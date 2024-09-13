# Loading libraries
import streamlit as st
import json

# Guarda el string base64 de la imagen en un archivo .txt una sola vez y luego carga el contenido de ese archivo
def open_image():
    with open("Images/Image_1_base64.txt", "r") as f:
        image_base64 = f.read()
        return image_base64
#----------------------------------------------------------------#
# Configuración de las páginas de la webapp
def page_configuration():
    st.set_page_config(page_title="CalcMaster",
                page_icon="Images/Logo.ico",
                layout="wide",
                initial_sidebar_state="auto")
#----------------------------------------------------------------#
# Configuración del sidebar
image_base64 = open_image()
def sidebar_elements():
    st.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] > div:first-child {{
            background: url(data:image/webp;base64,{image_base64});
            }}
            </style>
            """,
            unsafe_allow_html = True,
            ) # It is a url of a base64
    
    st.sidebar.title("CalcMaster WebApp 1.0")

    # Defining all the pages and the interface into the sidebar
    with st.sidebar:
        st.page_link(page="Central_app.py", label="Home", icon=":material/home:" )
        st.page_link(page="pages/functions.py", label="Funciones", icon=":material/monitoring:")
        st.page_link(page="pages/limit.py", label="Límites", icon=":material/query_stats:")

        st.divider()
        st.write("Aplicación Web para cálculo universitario")
#----------------------------------------------------------------#
# Imagen de la página de Inicio
@st.cache_resource
def imagen_inicio():
    st.image("Images/Logo_1.webp", width=500)
#----------------------------------------------------------------#
# Configuración de las animaciones
@st.cache_resource
def load_lottiefile(filename: str):
                with open(file=filename, mode='r') as f:
                    return json.load(f)
#----------------------------------------------------------------#
# Ocultando el botón de hamburguesa
@st.cache_resource
def hidding_hamburguer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility:hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#----------------------------------------------------------------#
# Ocultando el botón de GitHub
@st.cache_resource
def hidding_github():
    hide_github_icon = """
    <style>
    #GithubIcon {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility:hidden;}
    </style>
    """
    st.markdown(hide_github_icon, unsafe_allow_html=True)