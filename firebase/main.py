import streamlit as st
from firebase import firebase

firebase = firebase.FirebaseApplication('smart-steward-default-rtdb.firebaseio.com', None)
result = firebase.get('/cs', None)
st.write(result)
firebase.put("/","cs","1")
