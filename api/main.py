from bottle import route, run, template
import streamlit as st
from threading import Thread

st.write("API")

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

Thread(target = run).start()
