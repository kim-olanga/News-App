from distutils.debug import DEBUG

from instance.config import NEWS_API_KEY


class Config:
    """
    General parent configuration class
    """
    NEWS_API_BASE_URL = 'https://https://newsapi.org/news/{}?api_key={}'

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        config: The parent configuration class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    Args: 
        Config: The parent configuration  class with General configuration settings
    """

    DEBUG = True