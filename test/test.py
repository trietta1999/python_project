import subprocess, os
import streamlit as st

st.write(subprocess.call(os.getcwd()))
#st.write(subprocess.call(["cd","pages","&&","streamlit", "run", 'main.py']))

