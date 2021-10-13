import streamlit as st
import requests
import pandas as pd

txt = requests.get('https://archive.org/download/test_20211013_202110/test.csv').content
st.write(txt)

with open('test.csv','wb') as f:
  f.write(txt)

df = pd.read_csv('test.csv')
st.write(df['xmin'])
