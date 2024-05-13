from flask import Flask
from front_page.views import front_page
from config import DevelopmentConfig, ProductionConfig
import os
import logging


app = Flask(__name__)
if not os.environ.get('PRODUCTION'):
    app.config.from_object(DevelopmentConfig)
    app.logger.info('Development configuration loaded.')
    app.logger.info('See readme.md for more info.')
else:
    app.config.from_object(ProductionConfig)
    app.logger.info('Production configuration loaded.')


# Blueprints
app.register_blueprint(front_page)
