import os

class Config:
    DEBUG=True
    TESTING=True
    UPLOAD_FOLDER=os.path.realpath('.')+ '/aplication/templates/static/images/'
    # Configuration database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:jos84mar19@localhost:3306/imagenes"

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    DEBUG=True
    TESTING=True