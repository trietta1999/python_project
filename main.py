import streamlit as st
from PIL import Image
from io import BytesIO, StringIO
import os, time

os.system("pip install streamlit")

def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():
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
		if data_file is not None:
			st.write(type(data_file))
		#else: st.write("None")
	#st.info("Kết thúc chương trình")
	#st.info("Nhấn vào ≡ -> Rerun để chạy lại")
	
if __name__ ==  "__main__":
	main()
