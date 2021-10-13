import streamlit as st
import requests

txt = requests.get('https://archive.org/download/test_20211013_202110/test.csv').text
st.write(txt)
