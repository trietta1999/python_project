import streamlit as st
import requests, os
import pandas as pd

if (os.path.exists('test.jpg')==False):
  st.write("false")
  txt = requests.get('https://archive.org/download/mbid-a212af05-ac1c-478c-a8bf-9621681c13e6/mbid-a212af05-ac1c-478c-a8bf-9621681c13e6-30432369209_itemimage.jpg').content
  #st.write(txt)

  with open('test.jpg','wb') as f:
    st.write(f.write(txt))
    f.close()
else: st.write("true")

#df = pd.read_csv('test.csv')
#st.write(df['xmin'])
#with open('test.map','rb') as f:
#  st.download_button(label="Download image",data=f,file_name="game.map",mime="game/map")
