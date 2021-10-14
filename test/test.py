import subprocess, os
import streamlit as st

st.write(subprocess.call(["ls"]))
st.write(subprocess.call([os.chdir("pages"),"&&","streamlit", "run", 'main.py']))

