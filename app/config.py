import os
class Config:
    """
    General parent configuration class
    """
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apikey={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    
class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        config: The parent configuration class with General configuration settings
    """


class DevConfig(Config):
    """
    Development configuration child class
    Args: 
        Config: The parent configuration  class with General configuration settings
    """

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}