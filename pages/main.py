import streamlit as st# Create a page dropdown 
page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])
if page == "Page 1":
    st.wite("Display details of page 1")
elif page == "Page 2":
    st.wite("Display details of page 2")
elif page == "Page 3":
    st.wite("Display details of page 3")
