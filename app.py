import streamlit as st
import sys  

try:
    sys.path.remove("pages")
except: pass
try:
    sys.path.remove("yolo")
except: pass
try:
    del sys.modules["main", "detection"]
except: pass

app = st.selectbox("", ["Smart Steward", "YoloV4"])

if (app=="Smart Steward"):
    sys.path.append("pages")  
    from main import main
    main()
  
elif (app=="YoloV4"):
    sys.path.append("yolo")  
    from detection import main
    main()
