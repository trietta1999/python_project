import streamlit as st
import sys, os
import importlib

sys.path.append("pages")
sys.path.append("yolo")

app = st.selectbox("", ["Smart Steward", "YoloV4"])

if (app=="Smart Steward"):
    from main import main
    importlib.reload(main)
    main()
    
elif (app=="YoloV4"):
    from detection import main
    importlib.reload(detection)
    main()
