# src/langgraphagenticai/main.py
import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import Graph_Builder
from src.langgraphagenticai.ui.streamlitui.displayi_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else: 
        user_message = st.chat_input("Enter the Message")
    
    if user_message:
        # Check for API Key BEFORE trying to build the model
        if not user_input.get("GROQ_API_KEY"):
            st.error("Please enter your Groq API Key in the sidebar first!")
            return

        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            usecase = user_input.get("selected_usecase")
            graph_builder = Graph_Builder(model)
            graph = graph_builder.setup_graph(usecase)
            
            # Display results
            display_handler = DisplayResultStreamlit(usecase, graph, user_message)
            display_handler.display_result_on_ui()
                
        except Exception as e:
            st.error(f"System Error: {e}")