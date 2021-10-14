import subprocess, os
import streamlit as st

st.write(subprocess.run([os.chdir("pages"),"&&","streamlit", "run", 'main.py']))
st.write(subprocess.run(["ls"]))
