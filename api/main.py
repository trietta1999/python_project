import bottle
import streamlit as st
import threading

app = bottle.app()

@app.route('/data')
def get_data():
    return "data"

# Hiển thị dữ liệu trong giao diện Streamlit
st.title('Dữ liệu API')

# Chạy ứng dụng Bottle
if __name__ == '__main__':
    threading.Thread(target = lambda: app.run(port=8501)).start()
