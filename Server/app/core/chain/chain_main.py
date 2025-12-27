from langchain.agents import create_agent

from app.core.llm_config import models


agent = create_agent(
    model=models,
    system_prompt='你是一个有用的助手',
)