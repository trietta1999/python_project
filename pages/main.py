import streamlit as st
from posting import Posting
from tables import Tables


pages = {'tables':Tables,'posting':Posting}

choice = st.sidebar.radio("Choice your page: ",tuple(pages.keys()))

pages[choice]()
