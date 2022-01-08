# -*- coding: UTF-8 -*-
import streamlit as st
import sys

sys.path.append("fbchat_lib")
from fbchat_lib import Client

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
code = st.text_input("Mã xác thực:")
check = st.button("Đăng nhập")

if check:
	client = EchoBot("ttbotpython@gmail.com", "Triet@2312", code)
	#client.send(Message(text="Hi me!"), thread_id="100007572611070", thread_type=ThreadType.USER)
	#client = EchoBot("tadongthuyuyen@gmail.com", "Tatriet@0961475", "94474078")
	client.listen()
