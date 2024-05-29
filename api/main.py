from bottle import route, run, template
import streamlit as st

st.write("API")

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run()
