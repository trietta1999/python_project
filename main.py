import streamlit as st
import os

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")

col1, col2 = st.rows(2)

btn = col1.button("Enter")
btn2 = col1.button("Enter2")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
    st.write("Kết thúc chương trình")
    st.write("Nhấn vào ⫼ -> Rerun để chạy lại")
