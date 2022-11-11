import streamlit as st               
import seaborn as sns
import pandas as pd 
import plotly as px 

# import dataset
import plotly.express as px


# Creating the Figure instance
fig = px.line(x=[1,2, 3], y=[1, 2, 3])

# printing the figure instance
print(fig)


header = st.container()
with header:
    st.title("Plotly and streamlit  App:")
    st.text("Data")
df = px.data.gapminder()
st.write(df)
st.write(df.columns)

#Summary stat
st.wirte(df.describe())

# Data Managment

year_option = df['year'].unique().tolist()

year = st.selectbox("which year should we plot?", year_option, 0)

#df = df[df['year'] == year]

# plotting

fig = px.scatter(df , x='gdpPercap', y='lifeExp',size='pop', color='continent', hover_name='continent',
log_x=True, size_max=55, range_x=[100,100000], range_y=[20,90],
animation_frame='year', animation_group='country')

fig.update_layout(width=600)
st.write(fig)
