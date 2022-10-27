
from aplication import db
from flask import render_template,abort,send_from_directory,Blueprint, url_for,redirect
from fixtures.utils import get_register,insert_images,insert_images,insert_preserts
from aplication import app
from aplication.models.database import Image,Presert

init = Blueprint('/',__name__)


@init.route("/")
def index():
    total_images=Image.query.all()
    if len(total_images) == 0: 
            insert_images()
            return render_template("index.html")
    else:
        return render_template("index.html")
    

@init.route("/node")
def node():
    preserts = Presert.query.all()
    if preserts ==[]:
        add_preserts_images()
        return render_template("index.html")
    else:
        return render_template("index.html")


@init.route('/img',methods=["GET"])
def get_file():
    # data = {"id":int(request.args.get('id'))}
    # if "id" not in data:
    #     return jsonify({"message":"No ingreso el usarname"})
    # if  len(str(data["id"]))==0:
    #     return jsonify({"message":"No ingreso nada en el usuario"})
    name_file=get_register()
    if name_file!=None:
        return send_from_directory(app.config.get('UPLOAD_FOLDER'),path='1.jpg',as_attachment=False)
    else:
        abort(404)

