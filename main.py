import streamlit as st

btn = st.button("Enter")

while (1):
    try:
        ten = st.text_input("Nhập tên:")
        tuoi = st.text_input("Nhập tuổi:")
        #submitted = st.form_submit_button("Enter")
        if btn: st.write('on')
        else: st.write('off')
    except: pass

