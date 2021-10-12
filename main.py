import streamlit as st

while (1):
    try:
        ten = st.text_input("Nhập tên:")
        tuoi = st.text_input("Nhập tuổi:")
    except: pass
    btn = st.button("Enter")
    #st.text(btn)
    #btn = st.form_submit_button("Enter")
    if btn: st.write('on')
    else: st.write('off')
