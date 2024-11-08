import streamlit as st
import pandas as pd
import os
st.set_page_config(layout="wide")
# def save_message_to_log(book_title, message):
#    log_file = "message_log.txt"
 #   with open(log_file, "a") as file:
   #     file.write(f'{book_title}: {message}\n')
# def load_messages_from_log():
#    log_file = "message_log.txt"
#    if not os.path.exists(log_file):
#        return []
#    with open(log_file, "r") as file:
#        messages = file.readlines()
 #   return messages
#
df_reviews = pd.read_csv("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\dataset\customer reviews.csv")
df_top100_books = pd.read_csv("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\dataset\Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Selecione um livro", books)


df_book = df_top100_books[df_top100_books["book title"] == book]
df_books_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f'${df_book["book price"].iloc[0]}'
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)


col1, col2, col3 = st.columns(3)

col1.metric("Preço", book_price)
col2.metric("Ano", book_year)
col3.metric("Rating", book_rating)
st.feedback("stars")
st.divider()

for row in df_books_f.values:
    message = st.chat_message(f'{row[4]}')
    message.write(f'"**{row[1]}" - {row[2]}**')
    message.write(f'"{row[5]}"')


prompt = st.chat_input("Deixe um comentário")
if prompt:
    with st.chat_message("user"):
        st.write(f'{book_title} {prompt}'.strip())
    save_message_to_log(book_title, prompt)
st.logo("F:\linux Ubuntu\Linux Gabriel\Projeto em python de analise de dados\data\satto.png")

