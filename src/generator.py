from langchain.llms import BedrockClaude
import os

# Initialize Bedrock Claude LLM
def init_bedrock_llm():
    return BedrockClaude(
        model="Claude",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name="us-east-1"
    )
