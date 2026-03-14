import streamlit as st
from langchain_core.messages import HumanMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        # Prepare the input in the format LangGraph expects
        input_data = {"messages": [HumanMessage(content=self.user_message)]}

        if self.usecase == "Basic Chatbot":
            with st.chat_message("user"):
                st.write(self.user_message)

            with st.chat_message("assistant"):
                # Use a placeholder for the final response
                response_placeholder = st.empty()
                full_response = ""
                
                try:
                    # Explicitly pass input as a keyword argument to Pregel
                    for event in self.graph.stream(input=input_data):
                        for value in event.values():
                            # Extract the last message from the list
                            msgrist = value.get("messages", [])
                            if msgrist:
                                last_msg = msgrist[-1]
                                content = last_msg.content if hasattr(last_msg, 'content') else last_msg
                                full_response = content
                                response_placeholder.markdown(full_response)
                except Exception as e:
                    st.error(f"Error during streaming: {e}")