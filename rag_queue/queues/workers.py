from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
     collection_name="learning_rag",
       embedding=embedding_model,
)

def process_query(query:str):
    print("Searching Chunks", query)
    search_result = vector_db.similarity_search(query=user_query)
    context = "\n\n\n".join([f"Page content"])