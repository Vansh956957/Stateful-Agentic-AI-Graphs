import streamlit as st
st.set_page_config(page_title="Agentic AI langGraph", layout="wide")
with st.sidebar:
    # 1. Select LLM Dropdown
    selected_LLM = st.selectbox(
        "Selected LLM", options=["Groq", "OpenAI", "Anthropic"]

    )

    # 2. Select Model Dropdown
    select_model= st.selectbox(
        "Select Model", options=["llama", "mistral","Gemini"]
    )

    # 3. API key Input (Masked)
    # using type = Pasward auutomatically adds the eye icon to hide/show passward
    api_key = st.text_input(
        "API Key", type='password'
    )

    # 4. Usecase Drop down
    select_usecase = st.selectbox(
        "Usecase", options=["Basic Chatbot", "RAG Agent", "Coding Assistant"]

    )
