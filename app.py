import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

car_data = pd.read_csv("Vehicles_us.csv") # leer el archivo csv

# Encabezado de la aplicación
st.header("Análisis de Datos de Vehículos")

# Crear casillas de verificación en lugar de botones
show_histogram = st.checkbox("Mostrar Histograma de Precios")
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión (Año vs Precio)")

# Si se selecciona el histograma
if show_histogram:
    if "price" in car_data.columns:
        fig_hist = px.histogram(car_data, x="price", nbins="auto", title="Distribución de Precios de Vehículos",
                                labels={"price": "Precio (USD)"}, opacity=0.75)
        st.plotly_chart(fig_hist)
    else:
        st.error("No se encontró la columna 'price' en los datos.")

# Si se selecciona el gráfico de dispersión
if show_scatter:
    if "price" in car_data.columns and "model_year" in car_data.columns:
        fig_scatter = px.scatter(car_data, x="model_year", y="price", title="Relación entre Año del Vehículo y Precio",
                                 labels={"model_year": "Año del Vehículo", "price": "Precio (USD)"},
                                 opacity=0.6, color_discrete_sequence=["blue"])
        st.plotly_chart(fig_scatter)
    else:
        st.error("No se encontraron las columnas 'model_year' y/o 'price' en los datos.")

