import streamlit as st
import requests

txt = requests.get('https://archive.org/download/unnamed-asset-level-0-3234-mono-behaviour/unnamed%20asset-level0-3234-MonoBehaviour.txt', stream=True)
st.write(txt)
