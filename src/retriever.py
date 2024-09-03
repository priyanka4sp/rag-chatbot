import pinecone
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.retrievers import VectorDBRetriever

# Initialize Pinecone
def init_vector_retriever():
    pinecone.init(api_key="PINECONE_API_KEY", environment="us-west1-gcp")  # Replace with your environment

    # Connect to Pinecone index
    index = pinecone.Index("tech-support-index")
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')

    # Set up retriever
    retriever = VectorDBRetriever(
        embeddings=embeddings,
        index=index
    )
    return retriever
