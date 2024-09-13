# Charging libraries
import streamlit as st
import Utilities as utils
from Función_funciones import graficar_funcion

# -------------------- Setting the main page of the webapp -------------------- #
utils.page_configuration()
utils.hidding_hamburguer()
utils.hidding_github()
utils.sidebar_elements()

st.title(":blue[Gráfica de una función] 💹")
st.write("<h6 style = 'text-align:justify'> En esta sección de la aplicación podrás obtener la gráfica de una función, lo cual te permitirá distinguir de mejor manera el comportamiento de la función. </h6>", unsafe_allow_html=True)
st.divider()

with st.form(key="dominios"):
    st.subheader("Gráfica de una función", divider="rainbow")
    # variable = st.text_input(label="Define la variable de la función a evaluar", value="x", placeholder="x, y u otra variable")
    variable = st.multiselect(label="Define la variable de la función a evaluar", options=['x','y','z'], placeholder="Elige una opción")
    variable = str(variable)
    funcion = st.text_input(label="Función a evaluar", placeholder="Introduce una función")

    # Creating the button to evaluate the function
    Calculate_button = st.form_submit_button(label="Evaluar función", type="primary")

    if Calculate_button:
        try: 
            variable = variable[2]
            graficar_funcion(funcion_str=funcion, var_str=variable)
            print("Ok")
            # st.success("La función evaluada es:")
            # st.success(f"El dominio de la función en términos de {var_str} es: {dominio}")
        except:
            print("Algo no está bien, verficar el problema") # For terminal purposes
            st.error("""ERROR. Introduce una función correcta y verifica el uso adecuado de los operadores aritméticos al momento de escribir la función. Ejemplo:
                    
                    x^2+3*x+5/2""", icon="🚨")