import streamlit as st
import requests
import pandas as pd

txt = requests.get('https://archive.org/download/lumoria_b/lumoria_b.map').content
#st.write(txt)

with open('test.map','wb') as f:
  st.write(f.write(txt))

#df = pd.read_csv('test.csv')
#st.write(df['xmin'])
with open('test.map','wb') as f:
  st.download_button('Download binary file', f)
