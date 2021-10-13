import streamlit as st
import datetime, time, pytz, requests
from PIL import Image

def rerun(t):
    time.sleep(t)
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

page = st.selectbox("", ["Trang chủ", "Điều khiển", "Giám sát", "Thống kê"])

if page == "Trang chủ":
    st.write(datetime.datetime.now(pytz.timezone('Asia/Saigon')).strftime("%a %d/%m/%Y, %X"))
    image = Image.open(requests.get('https://hotondo.com.au/wp-content/uploads/2016/06/Header-1.jpg', stream=True).raw)
    st.image(image, caption='')
    
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        #st.markdown('<p style="font-family:sans-serif; font-size: 30px;">Nhiệt độ (°C)</p>', unsafe_allow_html=True)
        #st.markdown('<p style="font-family:sans-serif; color:Red; font-size: 50px;">00</p>', unsafe_allow_html=True)
        st.markdown("**Nhiệt độ (°C)**")
        st.write("00")
    with col2:
        st.write("Độ ẩm (%RH)")
        st.write("00")
        
    with col3:
        st.write("Thiết bị đang bật")
        st.write("0")
        
    with col4:
        st.write("Công suất tiêu thụ (Wh)")
        st.write("0.00")
        
    rerun(1)

elif page == "Page 2":
    st.write("Display details of page 2")
    b = st.button("Button")

elif page == "Page 3":
    st.write("Display details of page 3")
