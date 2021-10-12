import streamlit as st
import os

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
st.layout.columns:
    btn = st.button("Enter")
    btn2 = st.button("Enter2")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
st.write("Kết thúc chương trình")
st.write("Nhấn vào ⫼ -> Rerun để chạy lại")
