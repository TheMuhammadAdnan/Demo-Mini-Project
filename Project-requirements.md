# Demo Mini Project Documentation

## Overview

This document provides comprehensive information about the Demo Mini Project, a FastAPI application integrated with Shopify.

## Mini-Project Specifications

### Project Requirements

#### Objective:
Develop a FastAPI backend API with the route /orders/{customer_id}. This API will interact with a Shopify store to fetch and return order data for a specified customer ID in JSON format.

#### Targeted Skills:
- Python programming
- FastAPI framework usage
- Unit testing with pytest

#### Qualities:
We're looking for problem-solving ability, independent thinking, teamwork, adaptability, and eagerness to learn new technologies.

### Technical Requirements

1. **API Development:**
   - Build a FastAPI application with the endpoint /orders/{customer_id}.
   - Ensure the application is robust and handles various scenarios gracefully.

2. **Shopify API Integration:**
   - Use the provided API keys (`shop_url = "{ShopNameHere}.myshopify.com"`, `access_token = "{AccessTokenHere}"`) to connect to Shopify.
   - Fetch orders for customer IDs {Customer_ID}.

3. **Unit Testing with Pytest:**
   - Write comprehensive unit tests for your API using pytest.
   - Tests should cover various aspects of the API functionality, including edge cases.

### Evaluation Criteria

- **Code Quality:**
  - Clarity, structure, and maintainability of code.

- **Functionality:**
  - The API must meet all functional requirements, handle errors effectively, and perform as expected.

- **Testing:**
  - Quality and coverage of unit tests, ensuring thorough testing of the application.

### Submission Instructions

- Please submit your completed project via a GitHub repository.
- Provide a brief document explaining your approach, any challenges you faced, and how you resolved them.
- Ensure all unit tests are included and demonstrate successful execution.


Certainly! Below is a detailed document that you can add as a Markdown (.md) file in your GitHub repository:

## Project Structure

The project follows a clean and organized structure for ease of understanding and maintenance:

```
.
├── app
│   ├── api
│   │   ├── handlers
│   │   │   ├── health.py
│   │   │   ├── __init__.py
│   │   │   ├── orders.py
│   │   ├── __init__.py
│   │   └── router.py
│   ├── clients
│   │   ├── __init__.py
│   │   └── shopify_client
│   │       ├── __init__.py
│   │       └── shopify_client.py
...
├── tests
│   ├── __init__.py
│   └── test_orders.py
├── Demo Mini Project.postman_collection.json
├── docker-compose.yml
├── Dockerfile
├── logging.conf
├── main.py
├── Project-requirements.md
├── README.md
├── requirements.txt
```

### Key Directories:

- **app:** Contains the main application code.
- **tests:** Includes unit tests for the application.
- **Demo Mini Project.postman_collection.json:** Importable Postman collection for API testing.
- **docker-compose.yml:** Docker Compose configuration for easy deployment.
- **Dockerfile:** Configuration for building a Docker image.
- **logging.conf:** Configuration file for the custom logger.
- **main.py:** Entry point of the FastAPI application.
- **Project-requirements.md:** Project specifications and requirements.
- **README.md:** Main documentation file with instructions on running the application.

## How to Run the App

### Through Code

1. **Python Version:** 3.11.4

2. Inside the repository folder, activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add Shopify API keys:
   ```env
   SHOPIFY_ACCESS_TOKEN="{shopify_access_token}"
   SHOPIFY_SHOP_URL="{Shop_NAME}.myshopify.com"
   ```

5. Run the server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Through Docker-Compose

1. Build the Docker image:
   ```bash
   sudo docker build -t demo-mini-project .
   ```

2. Run the Docker image:
   ```bash
   sudo docker-compose up -d
   ```

Base URL for API calls: `http://0.0.0.0:8000/demo-mini-project/api/v1`

## Testing

Run tests using the command:
```bash
pytest
```

### Test Cases

1. **Get Orders by Customer ID (Success):**
   - Test successful retrieval of orders for a given customer ID.

2. **Get Orders by Customer ID (Limit Reached, Sleep):**
   - Test handling the case where the API call limit is reached, and the system sleeps before retrying.

3. **Get Orders by Customer ID (Invalid Status):**
   - Test handling an invalid status parameter when retrieving orders.

4. **Get Orders (Missing Customer ID):**
   - Test handling the case where the customer ID is missing in the request.

5. **Get Orders (Empty Response):**
   - Test handling an empty response when retrieving orders for a specific customer ID.

6. **Get Orders with Status:**
   - Test successful retrieval of orders for a given customer ID with a specific status.

## Additional Features

1. **Dockerization:**
   - Dockerized the application for easy deployment.

2. **Custom Logger:**
   - Implemented a custom logger for clean and easy-to-read logs.

3. **Exception Handling:**
   - Added a custom exception handler.

4. **Health Check Endpoint:**
   - Included a health check endpoint.

5. **Middleware:**
   - Added a sample middleware that logs whenever an endpoint is hit.

6. **Custom Response Generator:**
   - Utilized a custom response generator for well-structured API responses.

## Submission Details

- The completed project is available on [GitHub](https://github.com/TheMuhammadAdnan/Demo-Mini-Project).

- The README.md file provides detailed instructions on running the application and testing.

- Included documentation explains the approach, challenges faced, and their resolutions.

For any questions or clarifications, please feel free to reach out.

Thank you for the opportunity!

Best regards,
Muhammad Adnan
