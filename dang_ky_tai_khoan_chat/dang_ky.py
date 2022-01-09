import streamlit as st
from firebase import firebase
from time import sleep
import pyotp

totp = pyotp.TOTP(st.secrets["otp_secret"])
firebase = firebase.FirebaseApplication(st.secrets["firebase_link_project"], None)
st.write("ĐĂNG KÝ TÀI KHOẢN ĐIỀU KHIỂN NHÀ")

def rerun():
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

col1, col2 = st.columns(2)
uid = ''
with col1:
    uid = st.text_input("UID:")
with col2:
    st.info("1. Hướng dẫn lấy đường dẫn trang cá nhân Facebook tại [đây](https://www.thegioididong.com/game-app/cach-lay-link-trang-ca-nhan-fanpage-link-bai-viet-tren-1293304)")
    st.info("2. Lấy UID từ đường dẫn trang cá nhân Facebook tại [findidfb.com](https://findidfb.com/)")
    
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
        firebase.put("/", "request/code", code2)
        st.write("Đang đăng ký...")
        while(firebase.get('/request/success', None)==0): pass
        rerun()

if firebase.get('/request/success', None)==1:
    st.info("Đăng ký tài khoản thành công.")
    firebase.put("/", "request/success", 0)
elif firebase.get('/request/success', None)==2:
    st.error("Đăng ký tài khoản không thành công.")
    firebase.put("/", "request/success", 0)
