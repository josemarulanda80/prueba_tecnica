from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


app=Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


from aplication.views.start import bp

app.register_blueprint(bp)

db.create_all()