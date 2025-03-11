<<<<<<< HEAD
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Encabezado de la aplicación
st.title("Exploración de Datos de Vehículos")

# Mostrar datos
st.header("Vista previa de los datos")
st.dataframe(car_data)

# Casillas de verificación para gráficos
if st.checkbox("Mostrar Histograma"):
    st.write("Histograma del Odómetro")
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar Gráfico de Dispersión"):
    st.write("Gráfico de Dispersión: Precio vs Odómetro")
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig, use_container_width=True)
=======
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Encabezado de la aplicación
st.title("Exploración de Datos de Vehículos")

# Mostrar datos
st.header("Vista previa de los datos")
st.dataframe(car_data)

# Casillas de verificación para gráficos
if st.checkbox("Mostrar Histograma"):
    st.write("Histograma del Odómetro")
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar Gráfico de Dispersión"):
    st.write("Gráfico de Dispersión: Precio vs Odómetro")
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig, use_container_width=True)
>>>>>>> 035ec31798771439cbfe1c60f4c2cf915aca49d3
