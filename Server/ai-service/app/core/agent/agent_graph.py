
from langchain.agents import create_agent

from langchain_ollama import ChatOllama
from langgraph.graph import END, StateGraph,add_messages

from typing import TypedDict

model = ChatOllama(
    model='qwen3:0.6b',
)

class GirlState(TypedDict):
    human_message:str
    ai_message:str


def main(state:GirlState):
    state['human_message'] = 'hi my name is ' + state['human_message'] + ' I love you'
    return state

def llm(state:GirlState):
    llm = create_agent(
        model,
        system_prompt='你是我的女朋友,使用中文回复我的消息'
    )
    
    result = llm.invoke({'messages':state['human_message']})
    state['ai_message'] = result['messages'][-1].content
    return state


graph = StateGraph(GirlState)

graph.add_node("main",main)
graph.add_node("agent",llm)

graph.set_entry_point("main")
graph.add_edge("main",'agent')

graph.set_finish_point("agent")

app = graph.compile()

result = app.invoke({'human_message':"Gin"})


print(result)