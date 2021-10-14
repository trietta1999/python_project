import os
import subprocess
import sys

#from src.config import EnvironmentalVariableNames as EnvVar, get_env

def main():
    executable = sys.executable
    result = subprocess.run(
        f"{executable} -m streamlit run {os.path.join('pages', 'main.py')}",
        shell=True,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    main()
