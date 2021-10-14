import subprocess
import os
process = subprocess.Popen(["streamlit", "run", os.path.join('pages','main.py')])
