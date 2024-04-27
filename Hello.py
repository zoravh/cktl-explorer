
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Welcome",
        page_icon="👋",
    )

    st.write("# Welcome to your online Bartender! 👋")

    st.sidebar.success("Select a feature above.")

    st.markdown(
        """
        Welcome to your gateway to mastering the art of cocktail making. 
        By using this app, you'll not only broaden your drinking horizons and refine your palate but also dazzle your friends with your newfound mixology skills.
        
        This app was crafted by three university students eager to expand their horizons beyond the routine gin and tonics and screwdrivers. 
        Through developing this app, they broke free from the mundane, embracing a world of vibrant and diverse cocktails.
        
        ## How Does This App Work?
        The app boasts two core features designed to help you discover your perfect cocktail:
        
        ### Cocktail Search
        - **Search Function**: Allows you to look up a cocktail by name. If it exists in our extensive database, you can view detailed information including ingredients, preparation instructions, ideal glassware, and additional tips.
        
        ### Cocktail Filter
        - **Filter Function**: Enables you to find cocktails based on specific criteria such as the number of ingredients, preferred alcohol base, desired glassware, and the overall vibe of the cocktail. After setting your filters, the app will display all matching cocktails. Just click on one to see more about it, similar to the search function.
        
        Dive in and start exploring the rich world of cocktails with us!  
    """
    )


if __name__ == "__main__":
    run()
