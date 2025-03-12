import pandas as pd
import plotly.express as px
import streamlit as st
import csv

# Título
st.title("Mi Análisis Exploratorio de Datos")

# Archivo CSV a limpiar
csv_path = "vehicles_us.csv"

# Leer y limpiar el archivo CSV
with open(csv_path, "r") as file:
    lines = file.readlines()

cleaned_lines = [line for line in lines if not any(marker in line for marker in conflict_markers)]

# Guardar los cambios
with open(csv_path, "w") as file:
    file.writelines(cleaned_lines)

print(f"Conflictos eliminados en {csv_path}")


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


# Agregue una nueva parte del codigo para eliminar los conflictos en el archivo CSV, sin embargo
# no se si esta bien como tal, ya que elimine manualmente los datos que marcaban error en el archivo, lo intente en otro programa añadiendo cosas similares en el archivo
#pero en este proyecto no se si hubiera funcionado