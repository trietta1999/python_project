import streamlit as st

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

# col1, col2, col3 = st.columns(3)
# btn1 = col1.button("Enter1")
# btn2 = col2.button("Enter2")
# btn3 = col3.button("Enter3")
# static_store = get_static_store()

if btn:
	st.write("Bạn tên là %s, %s tuổi" % (ten, tuoi))
