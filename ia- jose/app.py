import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = linear_model.LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

st.title("Prevendo o valor de uma pizza!")
st.divider()

diametro = st.number_input("Digite o tamanho da pizza desejada ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'o valor da pizza é {preco_previsto:.2f}')
    st.balloons()