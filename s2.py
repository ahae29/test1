import streamlit as st
st.write("dasasdfsdafsdfsadfdsfsdffsdf")

st.write("dasasdfsdafsdfsadfdsfsdffsdf")
st.write("dasasdfsdafsdfsadfdsfsdffsdf")
st.write("dasasdfsdafsdfsadfdsfsdffsdf")
import pandas as pd

# 데이터 생성
data = {
    '열 1': ['A', 'B'],
    '열 2': ['C', 'D'],
    '열 3': ['E', 'F']
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 표 출력
st.table(df)
