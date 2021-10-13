import streamlit as st
from PIL import Image
from io import BytesIO, StringIO
from typing import Dict
import os, time

from firebase import firebase
firebase = firebase.FirebaseApplication('https://smart-steward-default-rtdb.firebaseio.com', None)
result = firebase.get('/cs', None)
st.write(result)

firebase.post('/cs', "",{"":0.99})

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
	"""This dictionary is initialized once and can be used to store the files uploaded"""
	return {}

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
static_store = get_static_store()

if btn:
	st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
# 	data_file = st.file_uploader("Upload")
# 	if data_file:
# 		c = data_file.getvalue()
# 		if not c in static_store.values():
# 			static_store[data_file] = data_file
# 	else:
# 		static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
# 		st.info("Upload one or more `.py` files.")
# 	for v in static_store.values():
# 		st.code(v)
	#	st.write(type(data_file))
	#else: st.write("None")
