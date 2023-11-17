import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image
"""Generación de la webapp con streamlit"""
#definir título
st.title("Título: Analítica de Datos")
#definir header
st.header("Este es un header")
st.subheader("Este es un header")
st.text("Texto: Hola Streamlit")
st.markdown("# Este es un markdown h1 ⧵n ## Este es un h2 ⧵n ### Este es un h3")
st.header("Colores de texto y mensajes de error")
st.success("Successful")
st.info("Información!")
st.warning("warning")
st.error("Error")
st.exception("NameError('no está definido')")
st.header("Obtener informacion de ayuda python")
st.help(range)
st.header("widgets: ")
st.subheader("Checkbox")
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Mostrar u ocultar Widget")
    st.subheader("Radio buttons")
# Radio Buttons
status=st.radio("Cual es su status", ("Activo", "Inactivo"))
if status == "Activo":
    st.succes("Estas activo")
else: 
    st.warning("Inactivo")
    st.subheader("SelectBox")
# SelectBox
occupation = st.selectbox(
"Tu Ocupacion", ["Programador", "Cientifico de datos", "BI", "Ingeniero de datos"]
    )
st.write("Opción seleccionada:", occupation)
st.subheader("Multiselect")
#Multiselect
location=st.multiselect(
    "Donde trabajas?",
    ("México", "Nueva York", "Guadalajara", "Monterrey", "Nepal", "Buenos Aires", "Caracas"),
)
st.write("Seleccionó:", len(location), "locaciones")
st.subheader("slider")
# slider
level=st.slider("Cual es tu nivel?", 1, 5)
