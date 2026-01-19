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
from langchain_core.messages import HumanMessage
# 输入 List  为聊天记录
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
    # tools=[msg_info,search_memory_tool],
    response_format=ai_response
)
def format_agent_output(agent_result):
    print('agent',agent_result)
    # 判断是否有格式化输出对象
    if isinstance(agent_result, dict) and 'model' in agent_result:
        model_data = agent_result['model']
        print(model_data['structured_response'].content)
        content = model_data['structured_response'].content
        return {
            'output': str(agent_result),
            'messages': str(content),
            'structured_response': model_data['structured_response']
        }
# 输入-agent-输出
agent_chain = RunnableLambda(input_adapter) | agent | RunnableLambda(format_agent_output)
app_with_history = RunnableWithMessageHistory(
    agent_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    output_messages_key="output", 
)