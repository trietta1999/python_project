import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["cd", "pages"]
    sys.argv = ["streamlit", "run", "main.py"]
    sys.exit(stcli.main())
