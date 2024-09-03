provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "rag_chatbot" {
  filename         = "${path.module}/lambda_deployment_package.zip"  # Path to your Lambda zip file
  function_name    = "RAGChatbot"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "src.lambda_handler.lambda_handler"
  runtime          = "python3.9"
  environment {
    variables = {
      AWS_ACCESS_KEY     = var.aws_access_key
      AWS_SECRET_KEY     = var.aws_secret_key
      PINECONE_API_KEY   = var.pinecone_api_key
      VECTOR_DB_ENDPOINT = "your-vector-db-endpoint"
    }
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "rag_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_exec_attach" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_apigatewayv2_api" "http_api" {
  name          = "RAGChatbotAPI"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.http_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.rag_chatbot.invoke_arn
}

resource "aws_apigatewayv2_route" "default_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /chat"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "pinecone_api_key" {}
