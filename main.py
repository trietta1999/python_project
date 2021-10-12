import streamlit as st
a=""
while(1):
  a = st.text_input("label goes here:")
  st.write(a)
  st.latex("\displaystyle\sum_{i=1}^{10} t_i")

