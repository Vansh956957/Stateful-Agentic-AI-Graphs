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

        # Handle BOTH Chatbot usecases (Basic and Web/Tool)
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