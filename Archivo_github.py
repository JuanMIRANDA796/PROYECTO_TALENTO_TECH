import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

#1. Configuración inical de la aplicacion

st.set_page_config(
  page_title = "👨‍🌾AgroIndustria",
  page_icon = " "
)
st.title("📊Dashboard AgroIndustria")
st.sidebar.title("Opciones de  navegación")

# 2. Generación de Datos Aleatorios
np.random.seed(42)
data = pd.DataFrame({
    "Fecha": pd.date_range(start="2024-01-01", periods=100, freq="D"),
    "Area": np.random.randint(100, 500, size=100),
    "Ubicacion": np.random.choice(["Andina", "Pacifica", "Caribe", "Orinoquia"], size=100),
    "Altitud": np.random.uniform(5, 30, size=100),
    "Región": np.random.choice(["Norte", "Sur", "Este", "Oeste"], size=100)
})

# 3. Implementación de la Barra de Navegación
menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Datos", "Visualización", "Configuración"]
)
