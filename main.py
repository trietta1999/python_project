import streamlit as st
import os

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")

# col1, col2, col3 = st.columns(3)
# btn1 = col1.button("Enter1")
# btn2 = col2.button("Enter2")
# btn3 = col3.button("Enter3")

btn = st.button("Enter")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
    t = st.file_uploader("Upload Image")
    st.write(t)
    #st.info("Kết thúc chương trình")
    #st.info("Nhấn vào ≡ -> Rerun để chạy lại")
