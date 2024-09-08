# Import necessary modules
from retriever import init_vector_retriever  # Initializes the vector database retriever
from generator import init_bedrock_llm       # Initializes the LLM from AWS Bedrock
from langchain.chains import RetrievalQA     # LangChain's module for combining retrieval and QA generation

def rag_chatbot(query):
    """
    Main function for the RAG chatbot.
    Takes a user query, retrieves relevant documents, and generates a response using LLM.
    
    :param query: The user's query as a string.
    :return: The generated response as a string.
    """
    # Initialize the vector retriever (Pinecone) and the LLM (Claude from AWS Bedrock)
    retriever = init_vector_retriever()
    llm = init_bedrock_llm()

    # Create a RAG chain by combining the retriever and the LLM
    rag_chain = RetrievalQA(
        retriever=retriever,         # The retriever to use for fetching relevant docs
        llm=llm,                     # The language model to generate answers
        retriever_max_docs=5         # Maximum number of docs to retrieve
    )

    # Run the RAG chain with the user's query to get a response
    response = rag_chain.run(query)
    return response

# Example usage of the RAG chatbot
if __name__ == "__main__":
    query = "How do I reset my device?"  # Example query
    print(f"Response: {rag_chatbot(query)}")  # Print the chatbot's response
