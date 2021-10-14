import subprocess, os
import streamlit as st
process = subprocess.Popen(["streamlit", "run", os.path.join('pages','main.py')])
st.write(process)
