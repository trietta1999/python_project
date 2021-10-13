import streamlit as st
import datetime, time

page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])
if page == "Page 1":
    #st.write(datetime.datetime.now())
    while (1):
        t = st.empty()
        for i in range(len(datetime.datetime.now()) + 1):
            t.markdown("## %s..." % text[0:i])
            time.sleep(0.1)
elif page == "Page 2":
    st.write("Display details of page 2")
    b = st.button("Button")
elif page == "Page 3":
    st.write("Display details of page 3")
