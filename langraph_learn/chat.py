from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    return {"message": ["Hi ,this is message from chatbot node"]}
def samplenode(state: State):
    return {"message": ["sample node appended"]}
graph_builder = StateGraph(State)
