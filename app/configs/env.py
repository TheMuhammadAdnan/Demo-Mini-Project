from pydantic import BaseSettings


class Environment(BaseSettings):
    APP_NAME: str = "demo-mini-project"
    LOGLEVEL: str = "DEBUG"

    # Shopify
    SHOPIFY_ACCESS_TOKEN: str
    SHOPIFY_SHOP_URL: str

    class Config:
        env_file = ".env"


env = Environment()
