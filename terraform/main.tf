# Define the AWS provider and region
provider "aws" {
  region = "us-east-1"  # Specify the AWS region for deployment
}

# Lambda function resource
resource "aws_lambda_function" "rag_chatbot" {
  filename         = "${path.module}/lambda_deployment_package.zip"  # Path to the zipped Lambda package
  function_name    = "RAGChatbot"                                    # Name of the Lambda function
  role             = aws_iam_role.lambda_exec.arn                   # IAM role with execution permissions
  handler          = "src.lambda_handler.lambda_handler"            # Entry point for the Lambda function
  runtime          = "python3.9"                                    # Runtime environment
  environment {
    variables = {  # Environment variables for the Lambda function
      AWS_ACCESS_KEY     = var.aws_access_key  # AWS access key
      AWS_SECRET_KEY     = var.aws_secret_key  # AWS secret key
      PINECONE_API_KEY   = var.pinecone_api_key  # Pinecone API key
      VECTOR_DB_ENDPOINT = "your-vector-db-endpoint"  # Endpoint for the vector database
    }
  }
}

# IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec" {
  name = "rag_lambda_role"  # Name of the IAM role

  # Policy to allow Lambda execution
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"  # Allow Lambda to assume this role
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"  # Specify Lambda service as the principal
        }
      }
    ]
  })
}

# Attach basic execution policy to the IAM role
resource "aws_iam_role_policy_attachment" "lambda_exec_attach" {
  role       = aws_iam_role.lambda_exec.name  # Attach policy to the Lambda execution role
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"  # Basic execution role policy
}

# API Gateway for exposing Lambda as a REST API
resource "aws_apigatewayv2_api" "http_api" {
  name          = "RAGChatbotAPI"  # Name of the API
  protocol_type = "HTTP"           # Protocol type (HTTP)
}

# API Gateway stage
resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id  # ID of the API
  name        = "$default"                        # Default stage
  auto_deploy = true                              # Automatically deploy the stage
}

# API Gateway integration with Lambda
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.http_api.id  # API ID
  integration
