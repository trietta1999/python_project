import subprocess, os
import streamlit as st

st.write(subprocess.run(["ls"]))
st.write(subprocess.run([os.chdir("pages"),"&&","streamlit", "run", 'main.py']))

