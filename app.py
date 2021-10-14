import streamlit as st
import sys, os
import importlib

sys.path.append("pages")
sys.path.append("yolo")

app = st.selectbox("", ["Smart Steward", "YoloV4"])

if (app=="Smart Steward"):
    import main
    importlib.reload(main)
    main.main()
    
elif (app=="YoloV4"):
    import detection
    importlib.reload(detection)
    detection.main()
