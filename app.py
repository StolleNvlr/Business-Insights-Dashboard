import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df_reviews = pd.read_csv("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\dataset\customer reviews.csv")
df_top100_books = pd.read_csv("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\dataset\Top-100 Trending Books.csv")

year_max = df_top100_books["year of publication"].max()
year_min = df_top100_books["year of publication"].min()
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()
st.sidebar.title("Menu")
max_price = st.sidebar.slider("Valor do Livro", price_min, price_max, price_max)
max_year = st.sidebar.slider("Ano de lançamento", year_min, year_max, year_max)

df_filtered = df_top100_books[(df_top100_books["book price"] <= max_price) & (df_top100_books["year of publication"] <= max_year)]

fig = px.bar(df_filtered["year of publication"].value_counts())
fig2 = px.histogram(df_filtered["book price"])


col1,col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

st.dataframe(df_filtered)
st.logo("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\data\satto.png")

