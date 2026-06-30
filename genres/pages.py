import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService

def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de Gêneros: ")
        genres_df = pd.json_normalize(genres) #json em DataFrame

        AgGrid(
            data =genres_df, 
        )
    else:
        st.warning('Nenhum gênero encontrado.')
    
    st.title('Cadastrar Novo Gênero')
    name = st.text_input("Digite o nome do gênero para buscar: ")
    if st.button("Cadastrar"):
        st.success(f"Cadastrando gênero: {name} com sucesso!")
