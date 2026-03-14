# src/langgraphagenticai/LLMs/groqllm.py
import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # We fetch using the EXACT keys defined in loadui.py
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get("selected_groq_model")

            if not groq_api_key:
                return None # Main.py will handle the error display

            return ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"LLM Init Error: {e}")