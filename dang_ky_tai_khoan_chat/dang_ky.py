import streamlit as st
from firebase import firebase
import pyotp

totp = pyotp.TOTP(st.secrets["otp_secret"])

firebase = firebase.FirebaseApplication(st.secrets["firebase_link_project"], None)

st.write("ĐĂNG KÝ TÀI KHOẢN ĐIỀU KHIỂN NHÀ")

col1, col2 = st.columns(2)
uid = ''
with col1:
    uid = st.text_input("UID:")
with col2:
    st.info("Lấy UID từ đường dẫn trang cá nhân Facebook tại [findidfb.com](https://findidfb.com/)")
    
col1, col2 = st.columns(2)
code1 = code2 = ''
with col1:
    code1 = st.text_input("Mã xác thực Google Authenticator:")
    code2 = st.text_input("Mã xác thực trên màn hình LCD:")
with col2:
    st.info("Lấy mã xác thực trong app Google Authenticator và mã trên màn hình LCD trong nhà")

dk = st.button("Đăng ký")
if dk:
    if totp.verify(code1):
        firebase.put("/", "request/re_uid", 1)
        firebase.put("/", "request/uid", uid)
