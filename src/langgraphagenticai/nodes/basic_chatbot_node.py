from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot logic Implementation
    """

    def __init__(self, model):
        self.llm = model
    
    def process(self, state: State) -> dict:
        """
        Process the input and generate a chatbot response.
        """
        # Wrap response in a list to ensure compatibility with add_messages
        response = self.llm.invoke(state['messages'])
        return {'messages': [response]}