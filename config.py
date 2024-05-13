import os
try:
    import env
except:
    env = {}
    pass


"""
Configuration settings for the Flask app.

Includes default, development, and production configurations.
For development, the SECRET_KEY is set in an env.py file.
For production, the SECRET_KEY is set in the environment variables.

Be sure to set a PRODUCTION=1 environment variable to use the production configuration.
"""

# Default
class BaseConfig(object):
    DEBUG = False


# Development
class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    PRODUCTION: any = None
    try:
        SECRET_KEY: str = env.SECRET_KEY
    except:
        raise ValueError('SECRET_KEY var is not set. Please create a file called env.py and add a SECRET_KEY: str variable.')
    SERVER_NAME: str = '127.0.0.1:5000'
    TRAP_BAD_REQUEST_ERRORS: bool = True
    TEMPLATES_AUTO_RELOAD: bool = True


# Production
class ProductionConfig(BaseConfig):
    DEBUG: bool = False
    PRODUCTION: any = os.environ.get('PRODUCTION')
    TRAP_BAD_REQUEST_ERRORS: bool = False
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    SERVER_NAME: str = os.environ.get('SERVER_NAME')
