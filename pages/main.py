import streamlit as st #Create a page dropdown 
page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])
if page == "Page 1":
    st.wite("Display details of page 1")
    a = st.text_input("Input")
elif page == "Page 2":
    st.wite("Display details of page 2")
    b = st.button("Button")
elif page == "Page 3":
    st.write("Display details of page 3")
