import streamlit as st
from PIL import Image
from io import BytesIO, StringIO
import os, time

def load_image(image_file):
	img = Image.open(image_file)
	return img

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")

# col1, col2, col3 = st.columns(3)
# btn1 = col1.button("Enter1")
# btn2 = col2.button("Enter2")
# btn3 = col3.button("Enter3")

btn = st.button("Enter")

if btn:
	st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
	data_file = st.file_uploader("Upload", type=['jpg'])
	file_details = st.empty()
	#content = data_file.getvalue()
	if not data_file:
		file_details.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
		return
	if isinstance(data_file, BytesIO):
		file_details.image(data_file)
	data_file.close()
	#else: st.write("None")
#st.info("Kết thúc chương trình")
#st.info("Nhấn vào ≡ -> Rerun để chạy lại")
