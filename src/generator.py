from langchain.llms import BedrockClaude  # Import Claude LLM from LangChain
import os                                 # For accessing environment variables

def init_bedrock_llm():
    """
    Initializes the Bedrock Claude LLM from AWS Bedrock.
    
    :return: A BedrockClaude LLM instance configured for use.
    """
    # Initialize the Claude LLM with AWS credentials
    # Ensure your AWS credentials are securely stored and accessed
    return BedrockClaude(
        model="Claude",                          # Specifying the Claude model
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),  # AWS Access Key from environment
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),  # AWS Secret Key from environment
        region_name="us-east-1"                  # AWS region
    )
