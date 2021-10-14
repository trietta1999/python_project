import streamlit as st
import sys, os
import importlib

sys.path.append("pages")
sys.path.append("yolo")

app = st.selectbox("Chọn App", ["Smart Steward", "YoloV4"])

if (app=="Smart Steward"):
    import pages
    importlib.reload(pages)
    pages.main()
    
elif (app=="YoloV4"):
    import detection
    importlib.reload(detection)
    detection.main()
