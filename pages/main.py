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
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    col1.write("")
    col3.write("")
    col5.write("")
    
    with col1:
        st.write("Nhiệt độ (°C)")
        b_nhietdo = st.button("00")
    
    rerun(1)

elif page == "Page 2":
    st.write("Display details of page 2")
    b = st.button("Button")

elif page == "Page 3":
    st.write("Display details of page 3")
