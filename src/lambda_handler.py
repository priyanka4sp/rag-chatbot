from rag_chatbot import rag_chatbot  # Import the main RAG chatbot function

def lambda_handler(event, context):
    """
    AWS Lambda handler function to process incoming requests.
    
    :param event: The event data passed by AWS Lambda (contains the query).
    :param context: The runtime information of the Lambda function.
    :return: Response containing the status code and the generated answer.
    """
    # Extract the query from the event data (assumes query is passed in JSON)
    query = event.get('query', '')
    
    # Return an error if the query is missing
    if not query:
        return {
            'statusCode': 400,
            'body': 'Query parameter is required'  # Return an error message for missing query
        }

    # Process the query using the RAG chatbot function
    response = rag_chatbot(query)
    
    # Return the generated response
    return {
        'statusCode': 200,
        'body': response  # Return the chatbot's response
    }
