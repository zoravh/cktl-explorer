# PAGE 02: COCKTAIL FILTER

# On this page, cocktails can be found via a filter mechanism

import streamlit as st
from utils import load_data
from utils import apply_filters
from utils import vibes
from utils import alcohol_bases

st.set_page_config(page_title="Cocktail Filter", page_icon="📊")
st.markdown("# Cocktail Filter")
st.sidebar.header("Cocktail Filter")
st.write(
    """Adapt the filters to match your liquor cabinet."""
)
    
df = load_data('https://github.com/OzanGenc/CocktailAnalysis/raw/main/cocktails.csv')

def display_cocktail_filter(df, alcohol_bases):
    glassware_options = ['Any'] + list(df['Glassware'].unique())
    max_ingredients = st.number_input('Maximum Ingredients', min_value=1, max_value=13, value=5, help="Select the maximum number of ingredients you want in your cocktails.")
    alcohol_base = st.selectbox('Select Alcohol Base', [a.strip().lower() for a in alcohol_bases])
    glassware = st.selectbox('Select Glassware', glassware_options)
    selected_vibe = st.selectbox('Select the Vibe of your drink', list(vibes.keys()))
    if st.button('Apply Filters'):
        filtered_df = apply_filters(df, max_ingredients, alcohol_base, glassware, selected_vibe)
        st.session_state['filtered_df'] = filtered_df  # Store the filtered DataFrame in session state

    if 'filtered_df' in st.session_state and not st.session_state['filtered_df'].empty:
        st.write("#### Here are your preferred drinks!")
        for i, row in st.session_state['filtered_df'].iterrows():
            if st.button(row['Cocktail Name'], key=f"btn_{i}"):  # Add a unique key to each button
                with st.container():
                    st.write(f"**Ingredients:** {row['Ingredients']}")
                    st.write(f"**Preparation:** {row['Preparation']}")
    else:  
        st.write("#### No cocktails found with the specified filters.")



display_cocktail_filter(df, alcohol_bases)


