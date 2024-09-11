# Loading libraries
import streamlit as st
import Utilities as utils
from streamlit_lottie import st_lottie

# -------------------- Setting the main page of the webapp -------------------- #
utils.page_configuration()
utils.hidding_hamburguer()
utils.hidding_github()
utils.sidebar_elements()

st.title(":green[CalcMaster WebApp] 👨‍🏫")
st.divider()

lottie_animation = utils.load_lottiefile("Gifs/Mathematics.json")
st_lottie(lottie_animation, height=200) # For more information about gifs you can check https://lottiefiles.com/

# utils.imagen_inicio()

with st.expander(label="Operadores de CalcMaster WebApp", icon="🔥"):
        st.write(":blue[Valor Absoluto] --> :orange[abs()]")
        st.write(":blue[Potencia] --> :orange[^]")
        st.write(":blue[Multiplicación] --> :orange[*]")
        st.write(":blue[Infinito] --> :orange[oo]")
        st.write(":blue[Raíz cuadrada] --> :orange[sqrt()]")

Author = "Aplicación desarrollada por el Dr. José Alberto Guzmán" 
st.write(f"<h4 style = 'text-align:center'> {Author} </h4>", unsafe_allow_html=True) 