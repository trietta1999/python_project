import bottle
import streamlit as st

app = bottle.app()

@app.route('/data')
def get_data():
    return "data"

# Hiển thị dữ liệu trong giao diện Streamlit
st.title('Dữ liệu API')

# Chạy ứng dụng Bottle
if __name__ == '__main__':
    app.run(port=8501)
