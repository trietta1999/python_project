import streamlit as st

while (1):
    try:
        with st.form("Test"):
            ten = st.text_input("Nhập tên:")
            tuoi = st.text_input("Nhập tuổi:")
            submitted = st.form_submit_button("Enter")
            if submitted:
                st.write("Bạn" + ten + " dễ thương quá," + tuoi + " rồi mà còn trẻ lắm!")
    except: pass

