# PAGE 01: COCKTAIL SEARCH

# On this page, cocktails can be found via a direct name-search

import streamlit as st
import streamlit as st
from utils import load_data

st.set_page_config(page_title="Cocktail Search", page_icon="📹")
st.markdown("# Cocktail Search")
st.sidebar.header("Cocktail Search")
st.write(
    """Type the name of your desired cocktail in the space below."""
)

df = load_data('https://github.com/OzanGenc/CocktailAnalysis/raw/main/cocktails.csv')
    
#  Tab 2 Search by title
def display_cocktail_search(df):
    search_query = st.text_input("Search for a cocktail")
    if search_query:
        # Perform a case-insensitive search within the 'Cocktail Name' column
        results = df[df['Cocktail Name'].str.contains(search_query, case=False, na=False)]
        if not results.empty:
            st.write("### Here's what you're looking for")
            for i, row in results.iterrows():
                if st.button(row['Cocktail Name']):
                    with st.container():
                        st.write(f"**Ingredients:** {row['Ingredients']}")
                        st.write(f"**Preparation:** {row['Preparation']}")

        else:
            st.write("No cocktails found with that name.")

display_cocktail_search(df)

