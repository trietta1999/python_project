import bottle, socket
import streamlit as st

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

app = bottle.app()

@app.route('/data')
def get_data():
    return "data"

# Chạy ứng dụng Bottle
if __name__ == '__main__':
    st.write(IPAddr)
    app.run(port=8502)
