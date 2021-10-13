import streamlit as st
import requests
import pandas as pd

txt = requests.get('https://archive.org/download/lumoria_b/lumoria_b.map').content
#st.write(txt)

with open('test.map','wb') as f:
  st.write(f.write(txt))
f.close()

#df = pd.read_csv('test.csv')
#st.write(df['xmin'])
with open('test.map','rb') as f:
  st.download_button(label="Download image",data=f,file_name="game.map",mime="game/map")
