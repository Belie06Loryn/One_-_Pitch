import os

class Config:
    SECRET_KEY = os.environ.get('ALEXIE')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/Pitchs'
    UPLOADED_PHOTOS_DESK ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:password@localhost/Pitchs_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:password@localhost/Pitchs'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig,
    'test':TestConfig
}