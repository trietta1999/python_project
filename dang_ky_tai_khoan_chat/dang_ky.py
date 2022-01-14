import streamlit as st
from firebase import firebase
from time import sleep, time
import pyotp

totp = pyotp.TOTP(st.secrets["otp_secret"])
firebase = firebase.FirebaseApplication(st.secrets["firebase_link_project"], None)
success = True

def rerun():
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

def wait(str0):
    global success
    success = True
    start = time()
    while(firebase.get(str0, None)==0):
        if (time() - start >= 10):
            success = False
            break
        sleep(0.001)
    if success == False: st.error("Hệ thống không hoạt động, hãy thử lại sau.")
    else: rerun()
    
page = st.selectbox("", ["Đăng ký tài khoản điều khiển nhà", "Đăng nhập từ xa"])

if page == "Đăng ký tài khoản điều khiển nhà":

    #st.write("ĐĂNG KÝ TÀI KHOẢN ĐIỀU KHIỂN NHÀ")
    #st.markdown('<p style="font-family:sans-serif; font-size: 30px;"><b>ĐĂNG KÝ TÀI KHOẢN ĐIỀU KHIỂN NHÀ</b><br></p>', unsafe_allow_html=True)

    st.info("Bước 1. Xem cách lấy ID người dùng Telegram của bạn tại [đây](https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-).")

    uid = st.text_input("ID người dùng Telagram:")

    st.info("Bước 2. Lấy mã xác thực trên màn hình LCD trong nhà và trong app Google Authenticator.")

    col1, col2 = st.columns(2)
    code1 = code2 = ''
    with col1:
        code2 = st.text_input("Mã xác thực trên màn hình LCD:")
    with col2:
        code1 = st.text_input("Mã xác thực Google Authenticator:")

    dk = st.button("Đăng ký")
    if dk:
        if (totp.verify(code1) or code1==st.secrets["test_code"]):
            st.write("Đang đăng ký...")
            firebase.put("/", "request/re_uid", 1)
            firebase.put("/", "request/uid", uid)
            firebase.put("/", "request/code", code2)
            wait("/request/success")
                               
        else: st.error("Hãy kiểm tra lại mã xác thực trong app Google Authenticator.")

    if firebase.get('/request/success', None)==1:
        st.info("Đăng ký tài khoản thành công.")
        firebase.put("/", "request/success", 0)
    elif firebase.get('/request/success', None)==2:
        st.error("Đăng ký tài khoản không thành công. Hãy kiểm tra lại UID/mã xác thực trên LCD và thử lại.")
        firebase.put("/", "request/success", 0)
        
if page == "Đăng nhập từ xa":
    st.info("Ghi \"/cmd xacthuc\" trong khung chat để lấy mã xác thực trong tin nhắn Telegram.")
    st.warning("Tài khoản của bạn phải đăng ký trước mới thực hiện được chức năng này.")
    
    col1, col2 = st.columns(2)
    code1 = code2 = ''
    with col1:
        code1 = st.text_input("Nhập mã xác thực trong tin nhắn Telegram:")
    with col2:
        code2 = st.text_input("Nhập mã xác thực trong app Google Authenticator:")
    dk = st.button("Đăng nhập")
    
    if dk:
        if (totp.verify(code2) or code2==st.secrets["test_code"]):
            st.write("Đang đăng nhập...")
            firebase.put("/", "login/code1", code1)
            firebase.put("/", "login/code2", code2)
            firebase.put("/", "login/re_login", 1)
            wait("/login/success")
            
        else: st.error("Hãy kiểm tra lại mã xác thực trong app Google Authenticator.")
        
    if firebase.get('/login/success', None)==1:
        st.info("Đăng nhập thành công.")
        firebase.put("/", "login/success", 0)
    elif firebase.get('/login/success', None)==2:
        st.error("Đăng nhập không thành công. Ghi \"/cmd xacthuc\" trong khung chat để lấy mã xác thực mới trong tin nhắn Telegram")
        firebase.put("/", "login/success", 0)
