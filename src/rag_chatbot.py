from retriever import init_vector_retriever
from generator import init_bedrock_llm
from langchain.chains import RetrievalQA

def rag_chatbot(query):
    # Initialize retriever and generator
    retriever = init_vector_retriever()
    llm = init_bedrock_llm()

    # Combine into a Retrieval-Augmented Generation chain
    rag_chain = RetrievalQA(
        retriever=retriever,
        llm=llm,
        retriever_max_docs=5  # Retrieve top 5 relevant documents
    )

    # Generate response based on retrieved documents
    response = rag_chain.run(query)
    return response

# Example usage
if __name__ == "__main__":
    query = "How do I reset my device?"
    print(f"Response: {rag_chatbot(query)}")
