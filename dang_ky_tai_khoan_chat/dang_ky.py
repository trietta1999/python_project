import streamlit as st
import pyotp

totp = pyotp.TOTP(st.secrets["otp_secret"])

st.write("ĐĂNG KÝ TÀI KHOẢN ĐIỀU KHIỂN NHÀ")

col1, col2 = st.columns(2)
uid = ''
with col1:
    uid = st.text_input("UID:")
with col2:
    st.info("Lấy UID từ đường dẫn trang cá nhân Facebook tại [findidfb.com](https://findidfb.com/)")
    
col1, col2 = st.columns(2)
code = ''
with col1:
    code = st.text_input("Mã xác thực:")
with col2:
    st.info("Lấy mã xác thực trong app Google Authenticator hoặc mã trên màn hình LCD trong nhà")

dk = st.button("Đăng ký")
if dk:
    if totp.verify(code): st.write()
