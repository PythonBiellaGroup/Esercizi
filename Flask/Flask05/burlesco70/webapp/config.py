import os
from pathlib import Path


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey"
    @staticmethod
    def init_app(app):
        pass    

class ProdConfig(Config):    
    pass

class DevConfig(Config):
    debug = True  
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")

class TestConfig(Config):
    debug = True  
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "testdata.sqlite")
    WTF_CSRF_ENABLED = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
