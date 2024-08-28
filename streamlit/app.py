import streamlit as st
import pandas as pd

st.title("hello streamlit")
st.write("this is streamlitgit add")


df = pd.DataFrame({
    'first col': [1, 2, 3, 4],
    'second col': [10, 20, 30, 40]
})

st.write("this is a dataframe")
st.write(df)
