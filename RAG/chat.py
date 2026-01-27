from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore



embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
     collection_name="learning_rag",
       embedding=embedding_model,
)
user_query = input("Ask something")

search_result = vector_db.similarity_search(query=user_query)

