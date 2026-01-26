from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
load_dotenv()
# 创建嵌入实例
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
)

# 测试嵌入
texts = ["这是一个测试句子，用于阿里云嵌入。"]
vectors = embeddings.embed_documents(texts)
print(f"向量维度: {len(vectors[0])}")  # 通常为1536

# 查询嵌入
query_vector = embeddings.embed_query("测试查询")
print(f"查询向量维度: {len(query_vector)}")