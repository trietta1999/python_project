import requests

txt = requests.get('https://colab.research.google.com/drive/1ksuBH5IVPBuR7Mxz96rxeSuE0hHLO-q1?usp=sharing', stream=True).raw
st.write(txt)
