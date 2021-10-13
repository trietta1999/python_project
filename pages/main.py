import streamlit as st
import datetime, time, threading

def time_update():
    while (1):
        st.write(datetime.datetime.now())
        time.sleep(1)
        
page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])
if page == "Page 1":
    t = threading.Thread(target=time_update)
    t = start()
elif page == "Page 2":
    st.write("Display details of page 2")
    b = st.button("Button")
elif page == "Page 3":
    st.write("Display details of page 3")
