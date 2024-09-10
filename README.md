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
Clone the repository to your local machine:

```bash
git clone https://github.com/priyanka4sp/rag-chatbot.git
cd rag-chatbot

### 2. Install Dependencies
Ensure you have Python installed (3.9 or later). Install the required Python packages:

pip install -r requirements.txt

### 3. Set Up Pinecone
-Sign Up: Create an account at Pinecone.
-Create an Index: Set up an index in Pinecone to store the document embeddings.
-API Key: Retrieve your Pinecone API key and add it to your environment variables.

export PINECONE_API_KEY="pinecone_api_key"


Here's the complete README.md file content formatted for direct placement in your Git repository. You can copy this content into a README.md file in your project directory.

markdown
Copy code
# **RAG-Based AI Chatbot for Technical Support**

This project implements a Retrieval-Augmented Generation (RAG) based AI chatbot designed to provide technical support for customers of a tech company specializing in consumer electronics. The chatbot helps users troubleshoot common issues, provides step-by-step guides, and offers information on warranty and repair services.

## **Features**

- **Retrieval**: Uses a vector database (Pinecone) to store and retrieve document embeddings.
- **Generation**: Integrates with AWS Bedrock (Claude) for generating contextually relevant responses.
- **Deployment**: Deployed on AWS using Lambda and API Gateway for scalable serverless operation.

## **Contents**

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Running Locally](#running-locally)
4. [Deploying to AWS](#deploying-to-aws)
5. [Testing the API](#testing-the-api)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)

## **Requirements**

- Python 3.9 or later
- AWS account with necessary permissions for Lambda, API Gateway, and IAM
- Terraform for infrastructure provisioning
- Pinecone account and API key
- AWS CLI configured with your credentials

## **Setup**

### **1. Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot

2. Install Dependencies
Ensure you have Python installed (3.9 or later). Install the required Python packages:

bash
Copy code
pip install -r requirements.txt

3. Set Up Pinecone
-Sign Up: Create an account at Pinecone.
-Create an Index: Set up an index in Pinecone to store the document embeddings.
-API Key: Retrieve your Pinecone API key and add it to your environment variables.

bash
Copy code
export PINECONE_API_KEY="your_pinecone_api_key"

4. Configure AWS
Ensure your AWS CLI is configured with the necessary permissions:

aws configure

5. Set Up Environment Variables
Set up the required environment variables for AWS access:

export AWS_ACCESS_KEY="aws_access_key"
export AWS_SECRET_KEY="aws_secret_key"

################################################## Running Locally ####################################################################

To run the RAG-based chatbot locally and test its functionality:

Run the Chatbot:
python src/rag_chatbot.py

Example Interaction:
You can modify the example query in rag_chatbot.py:

query = "How do I reset my device?"
print(f"Response: {rag_chatbot(query)}")

################################################# Deploying to AWS ################################################################

Deploying to AWS

1. Package the Lambda Function
Before deploying, package the Lambda function:

Zip the Source Files:
cd src
zip -r ../lambda_deployment_package.zip ./*

2. Deploy Using Terraform
The project includes a Terraform script (terraform/main.tf) to automate AWS deployment.

  - Navigate to the Terraform Directory:
    cd ../terraform

  - Initialize Terraform:
    Initialize Terraform to set up the provider plugins:

    terraform init

  - Review Terraform Plan:
    Preview the actions Terraform will take to deploy your resources:

    terraform plan

  - Apply the Terraform Configuration:
    Deploy the resources to AWS:

    terraform apply

Note: Confirm the deployment by typing yes when prompted. Terraform will output the API endpoint once deployment is complete.

3. Environment Variables in Terraform
Update the main.tf file in the terraform directory with your AWS credentials and other required variables before running terraform apply.

    variable "aws_access_key" {}
    variable "aws_secret_key" {}
    variable "pinecone_api_key" {}

Alternatively, you can provide these as command line arguments or via Terraform's .tfvars file.


#####################################################  Testing the API  ###############################################################
Testing the API

Once the API is deployed, you can test it using cURL, Postman, or any HTTP client.

Example Using cURL
Replace <API_ENDPOINT> with the actual endpoint provided by AWS API Gateway after deployment:

curl -X POST https://<API_ENDPOINT>/default/chat \
     -d '{"query": "How do I reset my device?"}' \
     -H "Content-Type: application/json"

Example Using Postman
- Create a new POST request.
- Set the URL: `https://<API_ENDPOINT>/default/chat`
- Add Headers:

        `Content-Type: application/json`

- Body:
          {
            "query": "How do I reset my device?"
          }

- Send the request and check the response.

##############################################  Troubleshooting  #####################################################
Troubleshooting

Issue: Lambda Errors
Solution: Check the AWS Lambda logs in CloudWatch for detailed error messages.

Issue: API Gateway 500 Error
Solution: Verify that all environment variables are correctly set and that the Lambda function has the necessary permissions.

Issue: Pinecone Connection Issues
Solution: Ensure that the Pinecone API key is correct and the index is properly configured.

###########################################################################################################################

Place this `README.md` file in your project's root directory to provide detailed setup and deployment instructions for users of your repository.
We can always enhance the existing code to make adjustments as per our requirements. Thank you! 

