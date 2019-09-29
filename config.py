import os

class Config:
    SECRET_KEY = 'ALEXIES'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/pitchs'
    UPLOADED_PHOTOS_DESK ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/pitchs'
    pass

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/pitchs'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/pitchs_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}