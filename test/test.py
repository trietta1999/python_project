import click, os
import streamlit.cli

@click.group()
def main():
    pass

@main.command("streamlit")
def main_streamlit():
    filename = os.path.join("pages, 'main.py')
    args = []
    streamlit.cli._main_run(filename, args)

if __name__ == "__main__":
    main()
