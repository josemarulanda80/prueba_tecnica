
from aplication import db
from flask import render_template,abort,send_from_directory,Blueprint, url_for,redirect
from fixtures.utils import get_register,insert_preserts
from aplication import app
from aplication.models.database import Presert

init = Blueprint('/',__name__)


@init.route("/")
def index():
    total_preserts=Presert.query.all()
    if len(total_preserts) == 0: 
            insert_preserts()
            return render_template("index.html",imagine=get_file(str(1)))
    else:
        return render_template("index.html",imagine=get_file(str(1)))
    
@init.route('/img/<name_file>',methods=["GET"])
def get_file(name_file):
        return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'{name_file}.jpg',as_attachment=False)
