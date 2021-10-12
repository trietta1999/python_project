import streamlit as st
a=""
while(1):
  a = st.text_input("label goes here:")
  st.write(a)
  st.latex("\int "+int(a)+" x^2 \,dx")

