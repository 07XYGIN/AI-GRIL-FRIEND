from app.core.database import SYNC_DATABASE_URL
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

def get_vector_store(user_id: str = None):
    
    return PGVector(
        embeddings=embeddings, 
        collection_name=user_id, 
        connection=SYNC_DATABASE_URL,
        use_jsonb=True,
    )

