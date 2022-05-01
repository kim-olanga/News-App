from distutils.debug import DEBUG


class Config:
    """
    General parent configuration class
    """
    pass

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