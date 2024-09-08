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
    retriever = VectorDBRetriever(import pinecone
from langchain.embeddings import SentenceTransformerEmbeddings  # For creating text embeddings
from langchain.retrievers import VectorDBRetriever             # LangChain's retriever interface

def init_vector_retriever():
    """
    Initializes the Pinecone vector database retriever.
    
    :return: A configured VectorDBRetriever instance.
    """
    # Initialize Pinecone with your API key and environment
    pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")  # Replace with your API key and environment

    # Connect to the Pinecone index created for storing document embeddings
    index = pinecone.Index("tech-support-index")  # Ensure this index exists in your Pinecone project

    # Initialize SentenceTransformer to create embeddings
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')

    # Set up the retriever with the Pinecone index and embedding model
    retriever = VectorDBRetriever(
        embeddings=embeddings,  # Embeddings model to convert text into vectors
        index=index             # Pinecone index to store and query vectors
    )
    return retriever

        embeddings=embeddings,
        index=index
    )
    return retriever
