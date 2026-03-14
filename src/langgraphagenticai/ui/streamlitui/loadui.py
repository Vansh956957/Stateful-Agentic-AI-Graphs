# src/langgraphagenticai/ui/streamlitui/loadui.py
import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        try:
            st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        except st.StreamlitAPIException:
            pass
            
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            self.user_controls["selected_llm"] = st.selectbox("Selected LLM", self.config.get_llm_options())

            if self.user_controls['selected_llm'] == 'Groq':
                # These keys must match the LLM class exactly
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", self.config.get_groq_model_options())
                self.user_controls['GROQ_API_KEY'] = st.text_input('API Key', type='password')

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please Enter your Groq API key.")

            self.user_controls['selected_usecase'] = st.selectbox("select usecases", self.config.get_usecase_options())
            
        return self.user_controls