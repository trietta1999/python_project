import streamlit as st

import os
os.system("ls")

import sys  
sys.path.append("pages")  
import main #scriptName without .py extension  

main.main()
