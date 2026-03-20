import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        input_data = {"messages": [HumanMessage(content=self.user_message)]}

        # Show user message immediately for all usecases
        with st.chat_message("user"):
            st.write(self.user_message)

        # Handle ONLY the standard Chatbot usecases (Basic, Web, Tool) here
        if self.usecase in ["Basic Chatbot", "Chatbot With Web", "Chatbot With Tool"]:
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""
                
                try:
                    # Use streaming for a better UI experience
                    for event in self.graph.stream(input=input_data):
                        for value in event.values():
                            msg_list = value.get("messages", [])
                            if msg_list:
                                last_msg = msg_list[-1]
                                
                                # If the agent is calling a tool (Web Search)
                                if isinstance(last_msg, ToolMessage):
                                    with st.status("🌐 Searching the web...", expanded=False):
                                        st.write(last_msg.content)
                                
                                # If the agent is replying to the user
                                elif isinstance(last_msg, AIMessage):
                                    if last_msg.content:
                                        full_response = last_msg.content
                                        response_placeholder.markdown(full_response)
                                        
                except Exception as e:
                    st.error(f"Graph Execution Error: {e}")

        # Handle the AI News usecase logic from the image
        elif self.usecase == "AI News":
            frequency = self.user_message
            
            with st.chat_message("assistant"):
                with st.spinner("Fetching and summarizing news... ⏳"):
                    # Use self.graph here instead of just graph since we are inside the class
                    result = self.graph.invoke({"messages": frequency})
                    
                    try:
                        # Read the markdown file
                        AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                        with open(AI_NEWS_PATH, "r") as file:
                            markdown_content = file.read()
                            
                        # Display the markdown content in Streamlit
                        st.markdown(markdown_content, unsafe_allow_html=True)
                        
                    except FileNotFoundError:
                        st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")