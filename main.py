import streamlit as st
from PIL import Image
from io import BytesIO, StringIO
import os, time

def load_image(image_file):
	img = Image.open(image_file)
	return img

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

# col1, col2, col3 = st.columns(3)
# btn1 = col1.button("Enter1")
# btn2 = col2.button("Enter2")
# btn3 = col3.button("Enter3")

if btn:
	st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
	data_file = st.file_uploader("Upload", type=['jpg'])
	if data_file:
		st.write(type(data_file))
	#else: st.write("None")
