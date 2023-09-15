import streamlit as st
import json

obj = {"x": 1, "y": 2}
st.write(obj)
st.write(json.dumps(obj))
