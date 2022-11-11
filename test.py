import streamlit as st               
import seaborn as sns
st.header("This video is brought to you by ijaz")

df = sns.load_dataset('iris')

st.write(df.head(10))

st.bar_chart(df['sepal_length'])

st.line_chart(df['sepal_length'])