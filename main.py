import streamlit as st

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

if btn:
    st.write('on')
else: st.write('off')
