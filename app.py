import streamlit as st
from genres.pages import show_genres
from actors.pages import show_actors
from movies.pages import show_movies
from reviews.pages import show_reviews
from login.page import show_login

def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        st.title("Flix App")
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Ínicio', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Séries', 'Avaliações' ]
        )

        if menu_option == 'Ínicio':
            st.write("Ínicio")

        if menu_option == 'Gêneros':
            show_genres()

        if menu_option == 'Atores/Atrizes':
            show_actors()

        if menu_option == 'Filmes':
            show_movies()

        if menu_option == 'Séries':
            st.write("Lista de Séries")

        if menu_option == 'Avaliações':
            show_reviews()



if __name__ == "__main__":
    main()

    
