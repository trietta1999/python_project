import streamlit as st
import os, pyautogui

os.system("pip uninstall pyqt5")
os.system("pip install pyautogui")
#os.system("python --version")

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")
btn2 = st.button("Chạy lại")

if btn:
    st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
st.write("Kết thúc chương trình")

if btn2:
    pyautogui.press('R')
