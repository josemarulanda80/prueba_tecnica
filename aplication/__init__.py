from flask import Flask,render_template,abort,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


app=Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


from aplication.views.start import init

app.register_blueprint(init)

db.create_all()