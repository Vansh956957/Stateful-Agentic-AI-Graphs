from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from langgraph.graph import START, END
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode

class Graph_Builder:
    def __init__(self, model):
        self.llm= model
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        """"
        Build a basic chatbot builder using  LangGraph.
        This method initializes a chatbot node using the "BasicChatBotNode"
        class and integrates it into the graph.The chatbot node is set as both
        the entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)


        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
        Build an Advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tools
        capabilites. And setup conditional and directional edges between nodes.
        The chatbot node is set as entry point.
        """

        ## Define Tool and Tool Node
        tools= get_tools()
        tool_node= create_tool_node(tools)

        # Define the LLM 
        llm = self.llm

        # Define the chatbot
        obj_chatbot__with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot__with_node.create_chatbot(tools)
        # Add the node
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")


    def setup_graph(self,usecase:str):
        """
        setup the graph for selected usecase.
        """
        self.graph_builder = StateGraph(State)
        if usecase== "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase=="Chatbot With Web":
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()

