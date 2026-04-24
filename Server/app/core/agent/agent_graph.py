from langgraph.graph import END, StateGraph,add_messages

from typing import TypedDict


class GirlState(TypedDict):
    human_message:str
    ai_message:str


def main(state:GirlState):
    state['ai_message'] = 'hi' + state['human_message'] + ' I love you'
    return state


graph = StateGraph(GirlState)

graph.add_node("main",main)

graph.set_entry_point("main")
graph.set_finish_point("main")

app = graph.compile()
