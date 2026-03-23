import os
from configparser import ConfigParser

class Config:
    # Use forward slashes so it works on both Windows and Linux/Streamlit Cloud
    def __init__(self, config_file='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        # Ensure the file exists before trying to read it
        if os.path.exists(config_file):
            self.config.read(config_file)
        else:
            print(f"Warning: Config file not found at {config_file}. Using defaults.")

    def get_llm_options(self):
        # Added a fallback string so it never returns None
        options = self.config['DEFAULT'].get('LLM_OPTIONS', 'Groq, OpenAI, Anthropic')
        return options.split(", ")
    
    def get_usecase_options(self):
        options = self.config['DEFAULT'].get('USECASE_OPTIONS', 'Default Usecase 1, Default Usecase 2')
        return options.split(", ")
    
    def get_groq_model_options(self):
        options = self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS', 'llama3-8b-8192, mixtral-8x7b-32768')
        return options.split(", ")
    
    def get_page_title(self):
        # No .split() here, but providing a default prevents Streamlit from showing a blank title
        return self.config['DEFAULT'].get("PAGE_TITLE", "Agentic AI Graph App")