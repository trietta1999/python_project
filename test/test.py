import subprocess, os
import streamlit as st

st.write(subprocess.call(os.getcwd()))
st.write(subprocess.call([os.chdir("/app/python/pages"),"pages","&&","streamlit", "run", 'main.py']))

