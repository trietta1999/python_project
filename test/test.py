import subprocess, os
import streamlit as st

#st.write(subprocess.call(os.getcwd()))
#st.write(subprocess.run([os.chdir("/app/python/pages"),"&&","streamlit", "run", 'main.py']))
subprocess.Popen(["streamlit", "run",os.path.join("/app/python/pages/main.py")])
