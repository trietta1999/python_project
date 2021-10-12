import streamlit as st

while (1):
  try:
    ten = st.text_input("Nhập tên:")
    tuoi = st.text_input("Nhập tuổi:")
    pst.write("Bạn",ten," dễ thương quá,",tuoi," rồi mà còn trẻ lắm!")
  except: pass

