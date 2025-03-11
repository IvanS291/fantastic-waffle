import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("Mi Análisis Exploratorio de Datos")

# Cargar datos
df = pd.read_csv("C:/Users/escor/fantastic-waffle/vehicles_us.csv")

# Mostrar columnas disponibles
st.write("Nombres de las columnas:")
st.write(df.columns)

# Mostrar tabla de datos
st.write("Aquí están los datos:")
st.dataframe(df)

# Gráfico ejemplo
fig = px.scatter(df, x="price", y="odometer", title="Precio vs. Kilometraje")
st.plotly_chart(fig)
