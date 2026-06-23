import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

movies = [
    {"id": 1, "name": "Rambo"},
    {"id": 2, "name": "Terminator"},
    {"id": 3, "name": "The Matrix"},
    {"id": 4, "name": "Forrest Gump"},
]

def show_movies():
    st.write("Lista de Filmes: ")

    AgGrid(
        data = pd.DataFrame(movies),
        reload_data = True,
        key = 'movies_grid',
    )
    
    st.title('Cadastrar Novo Filme')
    
    name = st.text_input("Digite o nome do filme para buscar: ")
    if st.button("Cadastrar"):
        st.success(f"Cadastrando filme: {name} com sucesso!")