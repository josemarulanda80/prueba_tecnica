from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


from aplication.views.start import bp

app.register_blueprint(bp)

db.create_all()