# Utils page

# import necessary packages and functions
import streamlit as st
import pandas as pd
import requests
import re
from io import StringIO

# function to load data from a URL into a DataFrame
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

# Lists of filtered variables that were created by us authors, not in the original database

# Alcohol
alcohol_bases = ['Any', ' Vodka ', ' Rum ', ' Gin ', ' Tequila ', ' Whiskey ', ' Brandy ', ' Vermouth ', ' Liqueurs ', ' Absinthe ', ' Aquavit ', ' Sake ', ' Sherry ', ' Port ', ' Cachaca ', ' Pisco ', ' Mezcal ']

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

# Functions to filter the dataframe 
def ingredient_in_phrase(phrase, ingredients_list):
    phrase = phrase.lower()
    patterns = [re.escape(ingredient) for ingredient in ingredients_list]
    return any(re.search(pattern, phrase) for pattern in patterns)

def apply_filters(df, max_ingredients, alcohol_base, glassware, selected_vibe):
    filtered_df = df[df['Ingredients'].apply(lambda x: len(x.split(',')) <= max_ingredients)]
    if alcohol_base != 'any':
        regex_pattern = r'\b' + re.escape(alcohol_base.strip().lower()) + r'\b'  
        filtered_df = filtered_df[filtered_df['Ingredients'].str.lower().str.contains(regex_pattern)]
    if glassware != 'Any':
        filtered_df = filtered_df[filtered_df['Glassware'] == glassware]
    if selected_vibe != 'Any':
        filtered_df = filtered_df[filtered_df['Ingredients'].apply(lambda x: ingredient_in_phrase(x, vibes[selected_vibe]))]
    return filtered_df

