
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app as _app
from app.clients.shopify_client.shopify_client import shopify_get_request



@pytest.fixture
def test_client():
    return TestClient(_app)

def test_get_orders_by_customer_id_success(test_client):
    customer_id = 123
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "mocked_orders_response"}


    # Mock the shopify_get_request function
    with patch('app.clients.shopify_client.shopify_client.shopify_get_request', return_value=mock_response):
        # Make the request to the FastAPI endpoint
        response = test_client.get(f"/demo-mini-project/api/v1/orders/{customer_id}")

    assert response.status_code == 200
    assert response.json().get("data", {}) == {'result': mock_response.json.return_value}

def test_get_orders_by_customer_id_limit_reached_sleep(test_client):
    customer_id = 123
    status = 'any'
    expected_url = f'/demo-mini-project/api/v1/orders/{customer_id}/orders.json?status={status}'

    # Mock the shopify_get_request function to simulate reaching API call limit
    with patch('app.clients.shopify_client.shopify_client.shopify_get_request', side_effect=[
        MagicMock(headers={'X-Shopify-Shop-Api-Call-Limit': '39/40'}),
        MagicMock(headers={'X-Shopify-Shop-Api-Call-Limit': '40/40'}),
        MagicMock(headers={'X-Shopify-Shop-Api-Call-Limit': '41/40'}),
    ]):

        # Make the request to the FastAPI endpoint
        response = test_client.get(f"/demo-mini-project/api/v1/orders/{customer_id}")

    assert response.status_code == 200

    

def test_get_orders_by_customer_id_invalid_status(test_client):
    customer_id = 123
    invalid_status = 'invalid_status'

    # Make the request to the FastAPI endpoint with an invalid status
    response = test_client.get(f"/demo-mini-project/api/v1/orders/{customer_id}?status={invalid_status}")

    assert response.status_code == 422
    assert response.json() == {'status': 'error', 'errors': 'Invalid status parameter', 'data': {}}


def test_get_orders_missing_customer_id(test_client):
    response = test_client.get("/demo-mini-project/api/v1/orders/")

    assert response.status_code == 404
    assert response.json() == {'status': 'error', 'errors': 'Not Found', 'data': {}}


def test_get_orders_empty_response(test_client):
    customer_id = 123
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    with patch('app.clients.shopify_client.shopify_client.shopify_get_request', return_value=mock_response):
        response = test_client.get(f"/demo-mini-project/api/v1/orders/{customer_id}")

    assert response.status_code == 200
    assert response.json() == {'status': 'success', 'errors': '', 'data': {'result': {}}}


def test_get_orders_with_status(test_client):
    customer_id = 123
    status = 'shipped'
    expected_url = f'/demo-mini-project/api/v1/orders/{customer_id}/orders.json?status={status}'
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "mocked_orders_response"}

    with patch('app.clients.shopify_client.shopify_client.shopify_get_request', return_value=mock_response):
        response = test_client.get(f"/demo-mini-project/api/v1/orders/{customer_id}?status={status}")

    assert response.status_code == 200
    assert response.json().get("data", {}) == {'result': mock_response.json.return_value}
