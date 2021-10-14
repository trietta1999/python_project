import sys
from streamlit import cli as stcli
import streamlit as st

def main():
    st.write("fg")

if __name__ == '__main__':
    sys.argv = ["cd", "pages"]
    sys.argv = ["streamlit", "run", "main.py"]
    sys.exit(stcli.main())
