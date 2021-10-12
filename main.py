import streamlit as st

@st.cache(allow_output_mutation=True)
def button_states():
    return {"pressed": None}

ten = st.text_input("Nhập tên:")
tuoi = st.text_input("Nhập tuổi:")
btn = st.button("Enter")

while (1):

    is_pressed = button_states()
    if btn: is_pressed.update({"pressed": True})
    if is_pressed["pressed"]:
        st.write('on')
        is_pressed.update({"pressed": False})
    #else: st.write('off')
