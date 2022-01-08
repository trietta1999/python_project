# -*- coding: UTF-8 -*-
import streamlit as st
import sys, os, importlib

sys.path.append("fbchat_lib")
from fbchat_lib import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		#log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		st.write(message_object.text)

		# If you're not the author, echo
		if author_id != self.uid:
			self.send(message_object, thread_id=thread_id, thread_type=thread_type)


client = EchoBot("tadongthuyuyen@gmail.com", "Tatriet@096147")
client.listen()
