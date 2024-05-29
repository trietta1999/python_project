import bottle, requests
import streamlit as st

app = bottle.app()

@app.route('/data')
def get_data():
    return "data"

# Chạy ứng dụng Bottle
if __name__ == '__main__':
    st.write(requests.get('https://api.ipify.org').content.decode('utf8'))
    app.run(port=8502)
