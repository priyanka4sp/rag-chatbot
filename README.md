# RAG-Based AI Chatbot for Technical Support

This project implements a Retrieval-Augmented Generation (RAG) based AI chatbot designed to provide technical support for customers of a tech company specializing in consumer electronics. The chatbot helps users troubleshoot common issues, provides step-by-step guides, and offers information on warranty and repair services.

## Features

- Uses a vector database (Pinecone) to store and retrieve document embeddings.
- Integrates with AWS Bedrock (Claude) for generating contextually relevant responses.
- Deployed on AWS using Lambda and API Gateway.

## Contents

1. Requirements
2. Setup
3. Running Locally
4. Deploying to AWS
5. Testing the API
6. Troubleshooting
7. License
  
## Requirements

- Python 3.9 or later
- AWS account with necessary permissions for Lambda, IAM and API Gateway
- Terraform for infrastructure provisioning
- Pinecone account and API key
- AWS CLI configured with your credentials

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/priyanka4sp/rag-chatbot.git
cd rag-chatbot

**## 2. Install Dependencies**

Ensure you have Python installed (3.9 or later). Install the required Python packages:

pip install -r requirements.txt

