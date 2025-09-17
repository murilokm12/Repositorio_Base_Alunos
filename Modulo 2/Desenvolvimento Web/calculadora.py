import streamlit as st

st.sidebar.text('Calculadora')

numb1 = st.text_input("Digite um número")
numb2 = st.text_input("Digite outro número")


colunas = st.columns(4)  

with colunas[0]:
    if st.button('adicao '):
     soma= float(numb1) + float(numb2)
     st.write(soma)