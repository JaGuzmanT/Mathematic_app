# Loading libraries
# Esta app corre en el environment: Streamlit --ROG STRIX
import streamlit as st
import Utilities as utils
from streamlit_lottie import st_lottie

# -------------------- Setting the main page of the webapp -------------------- #
utils.page_configuration()
utils.hide_elements()
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