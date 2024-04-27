# PAGE 02: COCKTAIL FILTER

# On this page, cocktails can be found via a filter mechanism

import streamlit as st

from utils import load_data
from utils import vibes
from utils import alcohol_bases

st.set_page_config(page_title="Cocktail Filter", page_icon="📊")
st.markdown("# Cocktail Filter")
st.sidebar.header("Cocktail Filter")
    
df = load_data('https://github.com/OzanGenc/CocktailAnalysis/raw/main/cocktails.csv')

def filter_cocktails(df, max_ingredients=None, alcohol_base='Any', glassware='Any', vibe='Any', alcohol_bases=[], vibes=[]):
    
    # Filter for cocktails with up to the given maximum number of ingredients
    if max_ingredients is not None:
        df = df[df['Ingredients'].apply(lambda x: len(x.split(','))) <= max_ingredients]

    # Filter by alcohol base if not 'Any'
    if alcohol_base != 'Any':
        df = df[df['Ingredients'].str.lower().apply(lambda ing: any(alcohol.lower() in ing for alcohol in alcohol_bases))]

    # Filter by glassware if not 'Any'
    if glassware != 'Any':
        df = df[df['Glassware'] == glassware]

    # Filter by vibe if not 'Any'
    if vibe != 'Any':
        df = df[df['Ingredients'].apply(lambda x: any(v.lower() in x.lower() for v in vibes))]

    return df

# User input for filter
max_ingredients = st.number_input('Maximum Ingredients', min_value=1, max_value=13, value=5, help="Select the maximum number of ingredients you want in the cocktails.")
alcohol_base = st.selectbox('Select Alcohol Base', alcohol_bases).lower()
glassware_options = ['Any'] + df['Glassware'].dropna().unique().astype(str).tolist()
glassware = st.selectbox('Select Glassware', glassware_options)
vibe = st.selectbox('Select the Vibe of your drink', vibes)

filtered_df = filter_cocktails(df, max_ingredients=max_ingredients, alcohol_base=alcohol_base, glassware=glassware, vibe=vibe, alcohol_bases=alcohol_bases, vibes=vibes)

st.write("### Here are your preferred drinks!")
for i, row in filtered_df.iterrows():
    if st.button(row['Cocktail Name']):
        with st.container():
            st.write(f"**Ingredients:** {row['Ingredients']}")
            st.write(f"**Preparation:** {row['Preparation']}")

