import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """"
    Loads and Runs LangGraph Agentic AI Application  with streamlit UI.
    This function initializes the UI, handles user input, configures LLM Models,
    setups the graph based on  the selected usecase, and displays the output while
    implementing exception handling for robustness.
    """

    ### Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter the Message")