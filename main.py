import streamlit as st

while(1):
  try:
    a = st.text_input("label goes here:")
    st.write(a)
    st.latex("\displaystyle\sum_{i=1}^{10} t_i")
  except: pass

