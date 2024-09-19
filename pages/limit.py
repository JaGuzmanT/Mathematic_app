# Charging libraries
import streamlit as st
import Utilities as utils
import sympy as sp
from limit_function import limit_calculation

# -------------------- Setting the main page of the webapp -------------------- #
utils.page_configuration()
utils.sidebar_elements()

st.title(":green[Límites] 📈")
st.write("<h6 style = 'text-align:justify'> En esta sección podrás calcular el límite de una función. </h6>", unsafe_allow_html=True)
st.divider()

with st.form("Límite"):
    st.subheader("Límite de una función", divider="rainbow")
    variable = st.text_input(label="Define la variable con la que deseas trabajar", placeholder="x, y u otra variable")
    function = st.text_input(label="Función: ", placeholder="Introduce una función")
    valor = st.text_input(label="Define hacia donde tiende el límite", value=0)

    # Creating the button to calculate the limit
    Calculate_button = st.form_submit_button(label="Calcular límite",type="primary")

    # Setting the button
    if Calculate_button:
        try:
            limit, var_str, original_function, simplified_function, value  = limit_calculation(function_str=function, var_str=variable, value=valor)
            st.success("La función original es: ")
            st.latex(original_function)
            st.success(f"La función simplificada queda como: ")
            st.latex(simplified_function)
            st.divider()
            st.write("Proceso de sustitución")
            st.success(f"Reemplazando {variable} = {value} en la función simplificada tenemos:")
            resultado = st.empty()
            with resultado.container():
                st.latex(f"({sp.latex(simplified_function)}) \\rightarrow {sp.latex(limit)}")
                print(limit) # For terminal purposes
                if limit == sp.zoo:
                    st.write(":green[El límite es indeterminado, el resultado implica una singularidad.] 😅")
                else:
                    st.success(f"El valor del límite es: {limit}")
            
        except Exception as e:
            print("Algo no está bien") # For terminal purposes
            st.error("""Error al calcular, por favor usa operadores aritméticos al momento de escribir la función. Ejemplo:
                    
                    x^2+3*x+5/2""", icon="🚨")