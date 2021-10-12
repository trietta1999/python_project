import streamlit as st

@st.cache(allow_output_mutation=True)
def button_states():
    return {"pressed": None}

while (1):
    try:
        ten = st.text_input("Nhập tên:")
        tuoi = st.text_input("Nhập tuổi:")
        btn = st.button("Enter")
        is_pressed = button_states()
    except: pass
    if btn: is_pressed.update({"pressed": True})
    if is_pressed["pressed"]: st.write('on')
    #else: st.write('off')
