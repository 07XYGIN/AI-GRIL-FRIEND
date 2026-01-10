from app.core.database import SYNC_DATABASE_URL
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
vector_store = PGVector(
    embeddings=embeddings, 
    collection_name="550e8400-e29b-41d4-a716-446655440000", 
    connection=SYNC_DATABASE_URL,
    use_jsonb=True,
)

