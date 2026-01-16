from dotenv import load_dotenv
from langchain_core.runnables.history import RunnableWithMessageHistory
from app.utils.history import get_session_history
from app.schemas.response import ai_response
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from .prompt import SYSTEM_PROMPT
from .tools.message import msg_info
from .tools.search_momery import search_memory_tool
from .llm_config import llm
from langchain_core.runnables import RunnableLambda
from rich.console import Console
load_dotenv()
console = Console()
from langchain_core.globals import set_debug
# set_debug(True)
from langchain_core.messages import HumanMessage
def input_adapter(data: dict):
    history = data.get("history", [])
    user_input = data.get("input", "")
    console.print(f"Debug history: {history}")
    console.print(f"Debug user_input: {user_input}")
    
    messages = list(history)
    if user_input and user_input.strip() :
        messages.append(HumanMessage(content=user_input))
    console.print(f"Debug Messages: {messages}")
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
    if 'messages' in agent_result:
        for msg in agent_result['messages']:
            if hasattr(msg, 'type') and msg.type == 'ai':
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    for call in msg.tool_calls:
                        if call.get('name') == 'ai_response':
                            return {
                                'output': call['args'].get('content', ''),
                                'messages': agent_result['messages'],
                                'structured_response': agent_result.get('structured_response')
                            }
                if hasattr(msg, 'content') and msg.content:
                    return {
                        'output': msg.content,
                        'messages': agent_result['messages'],
                        'structured_response': agent_result.get('structured_response')
                    }
    return {
        'output': str(agent_result),
        'messages': agent_result.get('messages', []),
        'structured_response': agent_result.get('structured_response')
    }

agent_chain = RunnableLambda(input_adapter) | agent | RunnableLambda(format_agent_output)

app_with_history = RunnableWithMessageHistory(
    agent_chain, 
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    output_messages_key="output", 
)