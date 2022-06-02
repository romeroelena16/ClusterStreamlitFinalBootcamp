import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.title('Análisis Exploratorio de Datos')


df = pd.read_csv('./data/ClusterFinal.csv', sep=";")


marca_x_precio_normal = df.groupby('Marca')['Precio Normal'].count().sort_values(ascending=False)
df_marca = pd.DataFrame(marca_x_precio_normal)
marca_x_precio_normal_cambio = df_marca.rename(columns={'Precio Normal': 'Cantidad de Marcas'})
marca_x_precio_normal_fig = px.bar(marca_x_precio_normal_cambio,x= marca_x_precio_normal_cambio.index,y='Cantidad de Marcas',
                             height=400, width=800, text_auto='.2s',color=marca_x_precio_normal_cambio.index)
st.write(marca_x_precio_normal_fig , use_container_width = True)


fig = px.box(df, x = "Tienda", y="Precio Online",color="Tienda",
             height=400, width=800, points="all",template="plotly_dark") 

st.write(fig , use_container_width = True)