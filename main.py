import streamlit as st
#import os

#os.system("pip install streamlit --upgrade")
#os.system("python --version")

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

if btn:
    st.write('on')
else: st.write('off')
