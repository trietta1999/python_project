import streamlit as st
import sys, os
import importlib

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:


st.write(
		"Has environment variables been set:",
		os.environ["db_username"] == st.secrets["db_username"])

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
