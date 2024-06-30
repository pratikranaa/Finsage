# FinSage API Documentation

## Overview

The FinSage API provides endpoints for accessing personalized financial wellness information for Bank of Baroda customers.

## Authentication

All API requests require OAuth 2.0 authentication. Obtain an access token from the Bank of Baroda authentication service before making requests.

## Endpoints

### Get User Financial Health

Retrieves the financial health score and summary for a given user.

GET /api/user/{userId}/financial-health

Parameters:

- userId (path): The unique identifier of the user

Response:

```json
{
  "userId": "string",
  "financialHealth": {
    "score": number,
    "summary": "string",
    "areas": [
      {
        "name": "string",
        "score": number,
        "advice": "string"
      }
    ]
  }
}
```



### Get Personalized Financial Advice

Generates personalized financial advice based on the user's current financial situation.

POST /api/user/{userId}/advice

Request Body:

```json
{
  "goal": "string",
  "timeframe": "string"
}
```

Response:

```json
{
  "userId": "string",
  "advice": [
    {
      "category": "string",
      "recommendation": "string",
      "impact": "string"
    }
  ]
}
```

## Error Handling

The API uses standard HTTP status codes for error responses. Detailed error messages are provided in the response body.

## System Architecture Diagram Description:

The FinSage system architecture consists of the following components and data flows:

1. User Interaction Layer:

   - Mobile App and Web Interface: Users interact with FinSage through these front-end applications.
   - These interfaces communicate with the FinSage API Gateway.
2. API Gateway (Azure API Management):

   - Routes requests to appropriate microservices.
   - Handles authentication and rate limiting.
3. Microservices (deployed on Azure Kubernetes Service):

   - User Profile Service: Manages user data and preferences.
   - Financial Health Service: Calculates and tracks financial health scores.
   - Advice Generation Service: Produces personalized financial advice.
   - Goal Tracking Service: Manages user financial goals.
   - Gamification Service: Handles challenges and rewards.
4. Data Layer:

   - Azure Cosmos DB: Stores user profiles, financial data, and application state.
   - Azure Blob Storage: Stores static content like educational materials.
5. AI and Analytics:

   - Azure Machine Learning: Hosts the AI Financial Advisor model.
   - Azure Databricks: Performs batch processing and model training.
   - Azure Synapse Analytics: Handles complex queries and analytics.
6. Integration Layer:

   - Azure Logic Apps: Orchestrates workflows between FinSage and Bank of Baroda systems.
   - Azure Service Bus: Manages asynchronous communication between services.
7. Bank of Baroda Systems:

   - Core Banking System: Provides real-time account information.
   - Transaction Processing System: Feeds transaction data to FinSage.
   - Product Catalog: Provides information for product recommendations.
8. Security and Monitoring:

   - Azure Active Directory: Manages authentication and authorization.
   - Azure Key Vault: Stores secrets and encryption keys.
   - Azure Monitor: Provides logging and monitoring for all components.

Data Flow:

1. User actions in the mobile app or web interface trigger API calls to the API Gateway.
2. The API Gateway authenticates the request and routes it to the appropriate microservice.
3. Microservices process the request, interacting with the data layer and AI services as needed.
4. For real-time banking data, microservices communicate with Bank of Baroda systems through the integration layer.
5. AI Financial Advisor model processes user data to generate personalized insights and advice.
6. Results are aggregated and sent back through the API Gateway to the user interface.
7. Batch processes run on Azure Databricks to update models and generate reports.
8. All interactions are logged and monitored for security and performance optimization.

This architecture ensures scalability, security, and seamless integration with existing Bank of Baroda systems while providing a powerful platform for AI-driven financial wellness services.
