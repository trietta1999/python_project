import streamlit as st
import os

os.system("pip uninstall pyqt5")
os.system("pip install pyautogui")
#os.system("python --version")

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
#else: st.write('off')
