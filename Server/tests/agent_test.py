from ast import mod
from langchain.agents import create_agent
from llm import llm

model = create_agent(
    model=llm,
    system_prompt='你是一个有用的助手',
)

# result = model.invoke({
#     'messages':[{
#         'role':"user","content":"解释机器学习和ai的关系"
#     }]
# })

# print(result['messages'][1].content)


for check,msg in model.stream({
        'messages':[{
        'role':"user","content":"解释机器学习和ai的关系"
    }]},stream_mode="messages",
):
    print(check.content)
