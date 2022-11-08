import streamlit as st
from firebase import firebase
import time, random

firebase = firebase.FirebaseApplication('https://smart-steward-default-rtdb.firebaseio.com/', None)
# result = firebase.get('/cs', None)
# st.write(result)
a = random.randint(0,10)
firebase.put("/","cs",a)
time.sleep(0.5)
st.experimental_rerun()
