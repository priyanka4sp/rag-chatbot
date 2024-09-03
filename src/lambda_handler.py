from rag_chatbot import rag_chatbot

def lambda_handler(event, context):
    query = event.get('query', '')
    if not query:
        return {
            'statusCode': 400,
            'body': 'Query parameter is required'
        }

    response = rag_chatbot(query)
    return {
        'statusCode': 200,
        'body': response
    }
