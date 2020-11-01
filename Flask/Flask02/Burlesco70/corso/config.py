class Config(object):    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):    
    pass

class DevConfig(Config):
    debug = True  
    SQLALCHEMY_DATABASE_URI = "sqlite:///corso.db"
