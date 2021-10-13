import streamlit as st
import requests

txt = requests.get('https://drive.google.com/file/d/1ML1D8EfrIlI0Xf3CsdWzmkNf9twRX8od/view?usp=sharing', stream=True).raw
st.write(txt.getvalue())
