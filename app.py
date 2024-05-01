# importando as bibliotecas necessárias
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import streamlit_pandas as sp
import plotly_express as px

# título
st.title(':blue[Vehicle advertisements data]')

# introdução
st.markdown('''
    This is an application for data visualization.''')


# lendo os dados
data_vehicles = pd.read_csv('vehicles.csv')


# visualizando e filtrando os dados
# definindo formato dos widgets de filtragem
create_data = {"model_year": "multiselect",
               "model": "multiselect",
               "condition": "multiselect",
               "cylinders": "multiselect",
               "fuel": "multiselect",
               "transmission": "multiselct",
               "type": "select",
               "paint_color": "multiselect"
                }

all_widgets = sp.create_widgets(data_vehicles, create_data, ignore_columns=["date_posted", "days_listed", "is_4wd"])
res = sp.filter_df(data_vehicles, all_widgets)
st.header("DataFrame")
st.write(data_vehicles)

st.header("Filtered DataFrame")
st.write(res)


# adicionando cabeçalho da seção
st.subheader('Histograms')

# criando caixas de seleção
price = st.checkbox('Price')
odometer = st.checkbox('Odometer')

if price: # se a caixa de seleção for clicada
    # escrevendo uma mensagem
    st.write ('Creating a histogram for the column: price.')
    
    # criando um histograma
    fig = px.histogram(data_vehicles, x='price')
    
    # exibindo o histograma
    st.plotly_chart(fig, use_container_width=True)

elif odometer:
    # escrevendo uma mensagem
    st.write ('Creating a histogram for the column: odometer.')
    
    # criando um histograma
    fig = px.histogram(data_vehicles, x='odometer')
    
    # exibindo o histograma
    st.plotly_chart(fig, use_container_width=True)

else:
    print ('Select a column to view a histogram.')
    
    
    
# adicionando cabeçalho da seção
st.subheader('Scatter plot')

# criando um botão
price_odometer_button = st.button('Price vs Odometer')  

if price_odometer_button:
    # escrevendo uma mensagem
    st.write ('Creating a scatter plot for the columns: odometer vs price.')
    
    # criando um gráfico de dispersão
    fig = px.scatter(data_vehicles, x="odometer", y="price")

    # exibindo o gráfico
    st.plotly_chart(fig, use_container_width=True)