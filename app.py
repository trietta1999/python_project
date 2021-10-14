import streamlit as st
import sys, os
import importlib

sys.path.append("pages")
sys.path.append("yolo")

app = st.selectbox("", ["Smart Steward", "YoloV4"])

if (app=="Smart Steward"):
    importlib.reload(main)
    from main import main
    main()
    
elif (app=="YoloV4"):
    importlib.reload(detection)
    from detection import main
    main()
