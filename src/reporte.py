import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.title('Análisis Exploratorio de Datos')


df = pd.read_csv('./data/ClusterFinal.csv', sep=";")

proces_x_precio_normal = df.groupby('Procesador')['Precio Normal'].count().sort_values(ascending=False)
df_proces = pd.DataFrame(proces_x_precio_normal)
proces_x_precio_normal_cambio = df_proces.rename(columns={'Precio Normal': 'Cantidad de Procesador'})
proces_x_precio_normal_fig = px.bar(proces_x_precio_normal_cambio, x= proces_x_precio_normal_cambio.index, y='Cantidad de Procesador',template="plotly_dark",
                             height=400, width=800, text_auto='.2s',color=proces_x_precio_normal_cambio.index)
st.write(proces_x_precio_normal_fig , use_container_width = True)


marca_x_precio_normal = df.groupby('Marca')['Precio Normal'].count().sort_values(ascending=False)
df_marca = pd.DataFrame(marca_x_precio_normal)
marca_x_precio_normal_cambio = df_marca.rename(columns={'Precio Normal': 'Cantidad de Marcas'})

marca_x_precio_normal_fig = px.bar(marca_x_precio_normal_cambio,x= marca_x_precio_normal_cambio.index,y='Cantidad de Marcas',
                             height=400, width=800, text_auto='.2s',color=marca_x_precio_normal_cambio.index)
st.write(marca_x_precio_normal_fig , use_container_width = True)


fig = px.box(df, x = "Tienda", y="Precio Online",color="Tienda",
             height=400, width=800, points="all",template="plotly_dark") 

st.write(fig , use_container_width = True)


st.title('Análisis para cluster')


df_filtro_clust_1 = df[df.cluster_predicted<=2]
df_filtro_1 = df_filtro_clust_1.rename(columns={'cluster_predicted': 'Número de Clusters'})

fig1 = px.box(df_filtro_1, x = "Número de Clusters", y="Precio Online",color="Tienda",
              title="Distribución de precios online por cluster y tienda departamental",
             height=400, width=900, points="all",template="plotly_dark") 
st.write(fig1 , use_container_width = True)

df_filtro_clust_2 = df[df.cluster_predicted>2]
df_filtro_2 = df_filtro_clust_2.rename(columns={'cluster_predicted': 'Número de Clusters'})

fig2 = px.box(df_filtro_2, x = "Número de Clusters", y="Precio Online",color="Tienda",
              title="Distribución de precios online por cluster y tienda",
             height=400, width=900, points="all",template="plotly_dark") 
st.write(fig2 , use_container_width = True)