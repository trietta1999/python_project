import streamlit as st
import requests

txt = requests.get('https://archive.org/download/test_20211013_202110/test.csv',params=ploads).content
st.write(txt)
