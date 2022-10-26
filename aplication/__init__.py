from flask import Flask,render_template,abort,send_from_directory
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


from aplication.views.start import init

app.register_blueprint(init)

db.create_all()