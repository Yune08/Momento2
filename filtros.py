import pandas as pd
import streamlit as st

data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

st.dataframe(data)


'''1.Filtro de prestacion de servicios que sean oficiales'''

data1 = data[data["prestacion_servicio"] == "oficial"]
st.dataframe(data1)

'''2.Filtro de punta en ingles >50 y <75'''

data2 = data[(data['puntaje_ingles'] > 50) & (data['puntaje_ingles'] < 75)]
st.dataframe(data2)

'''3.Filtro donde la comuna sea popular y el puntaje global mayor a 250'''

data3 = data[(data['comuna'] == "popular") & (data['puntaje_global'] > 250)]
st.dataframe(data3)

'''4.Filtro de la tercera fila'''

data4 = data.loc[2]
st.dataframe(data4)

'''5.Filtrar solo el establecimiento col basico camino de paz'''

data5 = data[data["establecimiento"] == "col basico camino de paz"]
st.dataframe(data5)