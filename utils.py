
import inspect
import textwrap
import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Function to load data from a URL into a DataFrame
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)
        return df
    except requests.RequestException as e:
        st.error(f"Failed to retrieve data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


# Lists of filtered variables that were created by authors, not in the original database

# Alcohol
alcohol_bases = ['Any', ' Vodka ', ' Rum ', ' Gin ', ' Tequila ', ' Whiskey ', ' Brandy ', ' Vermouth ', ' Liqueurs ', 'Absinthe', 'Aquavit', 'Sake', 'Sherry', 'Port', 'Cachaca', 'Pisco', 'Mezcal']

# Vibe

vibes = {
        'fruity': [
                'lemon', 'lime', 'orange', 'berry', 'pineapple', 'mango', 'peach', 'apple',
                'grape', 'banana', 'passion fruit', 'fruit liqueur', 'cherry', 'pomegranate',
                'apricot', 'melon', 'kiwi', 'pear', 'fig', 'fruit juice', 'fruit', 'juice'
                            ],
        'tropical': [
                'coconut', 'pineapple juice', 'mango juice', 'passion fruit juice', 'papaya',
                'guava', 'lychee', 'rum', 'tiki bitters', 'banana liqueur', 'Malibu', 'cachaça',
                'tamarind', 'dragon fruit', 'star fruit', 'kumquat', 'coconut milk', 'coconut cream',
                'falernum', 'orgeat'
                            ],
        'sweet': [
                'syrup', 'sugar', 'honey', 'liqueur', 'grenadine', 'agave nectar', 'sweet vermouth',
                'cointreau', 'maraschino', 'soda', 'cola', 'vanilla'
                            ],
        'spicy': [
                'pepper', 'cayenne', 'jalapeno', 'jalapeño', 'ginger', 'cinnamon', 'horseradish',
                'spicy', 'spice', 'hot sauce', 'tabasco', 'chili', 'wasabi', 'sriracha'
                             ]
                }



# original in this document

def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))
