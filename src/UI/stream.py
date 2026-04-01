import streamlit as st
# st.title("Hello meow")
# st.text()


def show_text(text):
    st.text(text)


def ask_query():
    return st.text_input("Enter query : ")

# query = st.text_input("Enter query : ")
# print(query)