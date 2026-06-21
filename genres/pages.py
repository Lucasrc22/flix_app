import streamlit as st
import requests

genres = [
    {"genre_id": 1, "name": "Action"},
    {"genre_id": 2, "name": "Comedy"},
    {"genre_id": 3, "name": "Drama"},
    {"genre_id": 4, "name": "Fantasy"},
    {"genre_id": 5, "name": "Horror"},
    {"genre_id": 6, "name": "Mystery"},

]


def show_genres():
    st.write("Lista de Gêneros: ")

    st.table(genres)
    st.title('Cadastrar Gênero')
    
    name = st.text_input("Digite o nome do gênero para buscar: ")
    if st.button("Cadastrar"):
        st.success(f"Cadastrando gênero: {name} com sucesso!")
