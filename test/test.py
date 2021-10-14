import subprocess, os
import streamlit as st

st.write(subprocess.Popen(["cd","pages","&&","streamlit", "run", 'main.py']))
st.write(subprocess.Popen(["ls"]))
