# Charging libraries
import streamlit as st
import sympy as sp
import Utilities as utils

# -------------------- Setting the main page of the webapp -------------------- #
utils.page_configuration()
utils.hide_elements()
utils.sidebar_elements()

st.title(":green[Cálculo de Derivadas] 👨‍🏫")
st.html("""<h6 style = 'text-align:justify'>
        Aquí podras calcular la derivada de una función con respecto a una variable de tu elección.
        </h6>""")
st.divider()

# -------------------- Definiendo funciones para el cálculo de derivadaas -------------------- #
def calcular_derivada(funcion_str, var_str):
    # Definir la variable simbólica
    var = sp.symbols(var_str)
    
    # Convertir la cadena de texto a una función simbólica
    funcion = sp.sympify(funcion_str)
    
    # Mostrar la función original
    st.write("Función original:")
    st.latex(sp.latex(funcion))
    
    # Paso 1: Expandir la función (si es posible)
    funcion_expandida = sp.expand(funcion)
    if funcion != funcion_expandida:
        st.write("Paso 1: Expandir la función (si es aplicable):")
        st.latex(sp.latex(funcion_expandida))
    else:
        st.write("La función no requiere expansión.")
    
    # Paso 2: Simplificar la función (si es posible)
    funcion_simplificada = sp.simplify(funcion_expandida)
    if funcion_expandida != funcion_simplificada:
        st.write("Paso 2: Simplificar la función:")
        st.latex(sp.latex(funcion_simplificada))
    else:
        st.write("La función no se puede simplificar más.")
    
    # Paso 3: Calcular la derivada de la función
    derivada = sp.diff(funcion_simplificada, var)
    st.write("Paso 3: Calcular la derivada de la función:")
    st.latex(sp.latex(derivada))
    
    # Paso 4: Simplificar la derivada (si es posible)
    derivada_simplificada = sp.simplify(derivada)
    if derivada != derivada_simplificada:
        st.write("Paso 4: Simplificar la derivada:")
        st.latex(sp.latex(derivada_simplificada))
    else:
        st.write("La derivada no requiere simplificación adicional.")
    
    # Mostrar el resultado final
    st.success("🙋 La derivada final es:")
    st.latex(sp.latex(derivada_simplificada))
    
    return derivada_simplificada

# -------------------- Configurando la interfaz de la página -------------------- #
with st.form(key="Derivación"):
    st.subheader("Derivada de una función", divider="rainbow")
    variable = st.selectbox(label="Define la variable con respecto a la cual vas a derivar", options=['x','y','z'], placeholder="Elige una variable")
    variable = str(variable)
    funcion = st.text_input(label="Función", placeholder="Introduce la función a derivar")

    # Botón para calcular la derivada
    Derivada_button = st.form_submit_button(label="Derivar", type="primary")

    if Derivada_button:
        try:
            calcular_derivada(funcion_str=funcion, var_str=variable)
            print("Ok") # For terminal purposes
        except:
            print("Algo no está bien, verficar el problema") # For terminal purposes

