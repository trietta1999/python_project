# -*- coding: UTF-8 -*-
import streamlit as st
import sys

sys.path.append("fbchat_lib")
from fbchat_lib import Client
from fbchat_lib.models import *

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		st.write(message_object.text)

		# If you're not the author, echo
		if author_id != self.uid:
			message_object.text = "Đã nhận 🎉"
			self.send(message_object, thread_id=thread_id, thread_type=thread_type)

def rerun():
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))
			
client = ''
try:
	client = EchoBot(st.secrets["fb_uname"], st.secrets["fb_pass"], code)
except: pass
			
app = st.selectbox("Menu", ["Đăng ký tài khoản", "Kiểm thử chat"])
if (app=="Đăng ký tài khoản"):			
	uname = st.text_input("UID:")
	st.write("Lấy UID bằng link tài khoản FB tại đây: [findidfb.com](https://findidfb.com/)")
	dk = st.button("Đăng ký")
	
	col1, col2 = st.columns(2)
	code = ''
	with col1:
		code = st.text_input("Mã xác thực:")
	with col2:
		st.error("Mục này chỉ dành cho nhà phát triển, nếu nhập sẽ gây lỗi")
	
	col1, col2 = st.columns(2)
	check = ''
	with col1:
		check = st.button("Đăng nhập")
	with col2:
		st.error("Mục này chỉ dành cho nhà phát triển, nếu nhấn sẽ gây lỗi")
	
	if dk:
		st.warning("Bạn có muốn tiếp tục?")
		col1, col2 = st.columns(2)
		with col1:
			tt = st.button("Tiếp tục")
			if tt: client.send(Message(text="Cám ơn bạn đã đăng ký, bây giờ bạn có thể chat."), thread_id=uname, thread_type=ThreadType.USER)
			
		with col2:
			huy = st.button("Hủy bỏ")
			if huy: rerun()
		
	if check:
		client = EchoBot(st.secrets["fb_uname"], st.secrets["fb_pass"], code)	
	
#elif (app=="Kiểm thử chat"):
		client.listen()
