import requests
from app.infrastructure.logger import logger
from time import sleep
from tenacity import retry, stop_after_attempt, retry_if_exception_type, wait_fixed
from app.configs.env import env

def create_sesion():
    s = requests.Session()
    s.headers.update({
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': env.SHOPIFY_ACCESS_TOKEN,
    })

    def api_calls(r, *args, **kwargs):
        calls_limit = r.headers['X-Shopify-Shop-Api-Call-Limit']
        call_limit_list = calls_limit.split("/")
        if int(call_limit_list[0]) + 1 == int(call_limit_list[1]):
            logger.info("Limit Reached, Sleeping for 5 second")
            sleep(5)


    s.hooks["response"] = api_calls    
    return s

@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(requests.exceptions.RequestException,), wait=wait_fixed(1), reraise=True)
def shopify_get_request(url: str):
    s = create_sesion()
    r = s.get(url)    
    return r

def shopify_post_request(url: str, data: dict):
    s = create_sesion()
    r = s.post(url, json=data)

def get_orders_by_customer_id(customer_id: int, status: str = 'any'):

    s = create_sesion()
    response = shopify_get_request(f'https://{env.SHOPIFY_SHOP_URL}/admin/api/2021-04/customers/{customer_id}/orders.json?status={status}')
    return response

def get_customers():
    pass

def get_customer_by_id(customer_id: int):
    pass

def get_orders():
    return 
