import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {"id":1, "name":"Brad Pitt"},
    {"id":2, "name":"Angelina Jolie"},
    {"id":3, "name":"Leonardo DiCaprio"},
    {"id":4, "name":"Meryl Streep"},
    {"id":5, "name":"Tom Hanks"},
    {"id":6, "name":"Scarlett Johansson"},
    {"id":7, "name":"Silvester Stallone"},
]

def show_actors():
    st.write("Lista de Atores: ")

    AgGrid(
        data = pd.DataFrame(actors),
        reload_data = True,
        key = 'actors_grid',
    )
    
    st.title('Cadastrar Novo Ator/Atriz')
    
    name = st.text_input("Digite o nome do ator para buscar: ")
    if st.button("Cadastrar"):
        st.success(f"Cadastrando ator: {name} com sucesso!")