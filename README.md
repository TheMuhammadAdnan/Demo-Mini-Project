# Demo Mini Project

## Overview

This is the README for the Demo Mini Project, a FastAPI application integrated with Shopify.

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

4. Create a `.env` file in the root folder of the project and add the following variables:
   ```env
   SHOPIFY_ACCESS_TOKEN="{shopify_access_token}"
   SHOPIFY_SHOP_URL="{Shop_NAME}.myshopify.com"
   ```

5. Run the server:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Through Docker-Compose

1. Inside the repository folder, build an image of the service:
   ```bash
   sudo docker build -t demo-mini-project .
   ```

2. Run the built Docker image:
   ```bash
   sudo docker-compose up -d
   ```

Use the provided base URL and extend it with the specific endpoint URL to make API calls to that endpoint:
* BASE URL: `http://0.0.0.0:8000/demo-mini-project/api/v1`

## Testing


Run the tests using the following command:
```bash
pytest
```

### Test Cases

#### 1. Get Orders by Customer ID (Success)

Test the successful retrieval of orders for a given customer ID.

#### 2. Get Orders by Customer ID (Limit Reached, Sleep)

Test handling the case where the API call limit is reached and the system sleeps before retrying.

#### 3. Get Orders by Customer ID (Invalid Status)

Test handling an invalid status parameter when retrieving orders.

#### 4. Get Orders (Missing Customer ID)

Test handling the case where the customer ID is missing in the request.

#### 5. Get Orders (Empty Response)

Test handling an empty response when retrieving orders for a specific customer ID.

#### 6. Get Orders with Status

Test the successful retrieval of orders for a given customer ID with a specific status.
