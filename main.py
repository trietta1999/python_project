import streamlit as st
#import os

#os.system("pip install streamlit --upgrade")
#os.system("python --version")

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

if btn:
    st.write("Bạn tên là ",ten,", ",tuoi," tuổi", sep='')
#else: st.write('off')
