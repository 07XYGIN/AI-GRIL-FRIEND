from langchain_ollama import ChatOllama
models = ChatOllama(
    model="qwen3-vl:4b",
    temperature=0,
    top_p=1,
)