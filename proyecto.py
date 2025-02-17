import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

#1. Configuración inical de la aplicacion

st.set_page_config(
  page_title = "🖥️Dashboard Interactivo",
  page_icon = " "
)
st.title("📊Dashboard interactivo con Streamlit")
st.sidebar.title("Opciones de  navegación") 
