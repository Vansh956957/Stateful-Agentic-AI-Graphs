# src/langgraphagenticai/ui/streamlitui/loadui.py
import streamlit as st
from streamlit.errors import StreamlitAPIException 
from src.langgraphagenticai.ui.uiconfigfile import Config
import os 

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        try:
            # Fetch the title, fallback to a default string if it returns None
            raw_title = self.config.get_page_title() or "Agentic AI App"

            st.set_page_config(page_title=f"🤖 {raw_title}", layout="wide")

            
        except StreamlitAPIException as e:
            pass
        except Exception as e:
            # Catch the TypeError or any other unexpected errors
            st.error(f"Failed to load UI: {str(e)}")
            
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            self.user_controls["selected_llm"] = st.selectbox("Selected LLM", self.config.get_llm_options())

            if self.user_controls['selected_llm'] == 'Groq':
                # These keys must match the LLM class exactly
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", self.config.get_groq_model_options())
                self.user_controls['GROQ_API_KEY'] = st.text_input('API Key', type='password')
                # Validate API Key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please Enter your Groq API key.")
            # Usecase Selection
            self.user_controls['selected_usecase'] = st.selectbox("select usecases", self.config.get_usecase_options())
            if self.user_controls['selected_usecase'] == "Chatbot With Web" or self.user_controls['selected_usecase'] == "AI News":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]= st.text_input("TAVILY API KEY",type="password")

                #Validate API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ please Enter your TAVILY_API_KEY key to proceed. Don't have? Refer : https://app.tavily.com/home ")
            if self.user_controls['selected_usecase'] =="AI News":
                st.subheader("📰 AI News Explorer")
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📰 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    
                    st.session_state.timeframe  = time_frame

        return self.user_controls