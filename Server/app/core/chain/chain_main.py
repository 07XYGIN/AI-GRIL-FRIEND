from dotenv import load_dotenv
from rich.console import Console
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from config import llm
from .prompt import SYSTEM_PROMPT
from .tools.message import msg_info
from .tools.search_momery import search_memory_tool
from app.schemas.response import ai_response
from app.utils.history import get_session_history
load_dotenv()
console = Console()
def input_adapter(data: dict):
    history = data.get("history", [])
    user_input = data.get("input", "")
    messages = list(history)
    if user_input and user_input.strip() :
        messages.append(HumanMessage(content=user_input))
    return {"messages": messages}
agent = create_agent(
    model=llm,
    system_prompt=SYSTEM_PROMPT,
    response_format=ai_response,
    tools=[msg_info,search_memory_tool],
)
def format_agent_output(agent_result):
    if 'structured_response' in agent_result:
        structured = agent_result['structured_response']
        if hasattr(structured, 'content'):
            return {
                'output': structured.content,
                'messages': agent_result.get('messages', []),
                'structured_response': structured
            }

agent_chain = RunnableLambda(input_adapter) | agent | RunnableLambda(format_agent_output)

app_with_history = RunnableWithMessageHistory(
    agent_chain, 
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    output_messages_key="output", 
)