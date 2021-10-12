import streamlit as st
import os

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")

col1, col2,col3 = st.columns(3)

with col1: btn = st.button("Enter")
with col2: btn2 = st.button("Enter2")
with col3: btn3 = st.button("Enter2")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
    st.write("Kết thúc chương trình")
    st.write("Nhấn vào ⫼ -> Rerun để chạy lại")
