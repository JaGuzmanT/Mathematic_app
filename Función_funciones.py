# Loading the libraries
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import streamlit as st
import plotly.express as px

#------------------- Funciones function -------------------#
def graficar_funcion(funcion_str, var_str):
    # Definir la variable simbólica
    var = sp.symbols(var_str)
    
    # Convertir la cadena de texto a una función simbólica
    funcion = sp.sympify(funcion_str)
    
    # Mostrar la función en formato LaTeX usando st.latex
    latex_funcion = sp.latex(funcion)
    st.latex(f"f({var_str}) = {latex_funcion}")

    # Calcular las raíces reales de la función
    raices = sp.solveset(funcion, var, domain=sp.S.Reals)
    raices_reales = list(raices) if raices else "No existen raíces reales 😌"
    
    # Definir la función lambda para facilitar la evaluación numérica
    f_lambdified = sp.lambdify(var, funcion, 'numpy')
    
    # Crear un rango de valores para graficar
    x_vals = np.linspace(-15, 15, 500)
    y_vals = f_lambdified(x_vals)
    
    # Graficar la función
    fig = px.line(x=x_vals, y=y_vals, 
                labels={'x': var_str, 'y': f'f({var_str})'}  # Etiquetas personalizadas
                )
    st.plotly_chart(fig)
    # Mostrar las raíces en Streamlit
    st.write(f":green[Raíces reales de la función:] :orange[{raices_reales}] ")

    # # Figura con matplotlib
    # fig, ax = plt.subplots()
    # ax = plt.plot(x_vals, y_vals, label=f'f({var_str}) = {funcion_str}')
    # ax = plt.xlabel(var_str)
    # ax = plt.ylabel('f(x)')
    # ax = plt.title(f"Gráfica de $f({var_str}) = {sp.latex(funcion)}$")
    # ax = plt.axhline(0, color='black', linewidth=0.5)
    # ax = plt.axvline(0, color='black', linewidth=0.5)
    # ax = plt.legend()
    # ax = plt.grid(True)
    # st.pyplot(fig)
    
    # Mostrar la gráfica en Streamlit
