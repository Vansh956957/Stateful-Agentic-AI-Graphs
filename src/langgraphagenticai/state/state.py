from typing_extensions import TypedDict, List
from typing import Annotated
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the structure of the State used in graph
    """
    messages: Annotated[list,add_messages]