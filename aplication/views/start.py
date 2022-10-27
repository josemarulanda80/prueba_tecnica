
from aplication import db
from flask import render_template,abort,send_from_directory,Blueprint, url_for,redirect
from fixtures.utils import get_register,insert_preserts
from aplication import app
from aplication.models.database import Presert

init = Blueprint('/',__name__)


@init.route("/")
def index():
    total_images=Presert.query.all()
    if len(total_images) == 0: 
            insert_preserts()
            return render_template("index.html",total=get_file())
    else:
        return render_template("index.html",total=get_file())
    


@init.route('/img',methods=["GET"])
def get_file():
    name_file=get_register()
    print(name_file)
    if name_file!="Error: Not conexion":
        return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'{str(name_file)}.jpg',as_attachment=False)
    else:
        return None
