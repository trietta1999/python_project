import streamlit as st
import datetime, time, pytz

def rerun(t):
    time.sleep(t)
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

page = st.selectbox("", ["Trang chủ", "Điều khiển", "Giám sát", "Thống kê"])
if page == "Trang chủ":
    st.write(datetime.datetime.now(pytz.timezone('Asia/Saigon')).strftime("%a %d/%m/%Y, %X"))
    rerun(1)
elif page == "Page 2":
    st.write("Display details of page 2")
    b = st.button("Button")
elif page == "Page 3":
    st.write("Display details of page 3")
