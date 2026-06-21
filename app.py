import streamlit as st
from genres.pages import show_genres

def main():
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
        st.write("Lista de Atores/Atrizes")

    if menu_option == 'Filmes':
        st.write("Lista de Filmes")

    if menu_option == 'Séries':
        st.write("Lista de Séries")

    if menu_option == 'Avaliações':
        st.write("Lista de Avaliações")



if __name__ == "__main__":
    main()
