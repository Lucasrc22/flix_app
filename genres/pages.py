import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

genres = [
    {"id": 1, "name": "Ação"},
    {"id": 2, "name": "Comédia"},
    {"id": 3, "name": "Drama"},
    {"id": 4, "name": "Fantasia"},
    {"id": 5, "name": "Terror"},
    {"id": 6, "name": "Mistério"},

]


def show_genres():
    st.write("Lista de Gêneros: ")

    AgGrid(
        data = pd.DataFrame(genres), #Resumidamente, é usado para criar um DataFrame a partir da lista de dicionários "genres", onde cada dicionário representa uma linha de dados. O DataFrame é uma estrutura de dados tabular que facilita a manipulação e visualização dos dados.
        reload_data = True,
        key = 'genres_grid',
    )
    
    st.title('Cadastrar Novo Gênero')
    
    name = st.text_input("Digite o nome do gênero para buscar: ")
    if st.button("Cadastrar"):
        st.success(f"Cadastrando gênero: {name} com sucesso!")
