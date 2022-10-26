from aplication import db
from flask import render_template,abort,send_from_directory,Blueprint
from fixtures.utils import get_register
from aplication import app
from aplication.models.database import Image,Presert


def add_images_data_base():
    images=["1.jpg","2.jpg","3.jpg","4.jpg"]
    for i in range(0,4):
        new_image=Image(filename=images[i])
        db.session.add(new_image)
        db.session.commit()
    return "ed"

def add_preserts_images():
    preserts=[0.1,0.4,0.7,0.9]
    for i in preserts:
            new_preserts= Presert(img=1,value=i)
            db.session.add(new_preserts)
            db.session.commit()
    return "bien"

init = Blueprint('/',__name__)


@init.route("/")
def index():
    total_images=Image.query.all()
    if total_images == []: 
        add_images_data_base()
        add_preserts_images()
    else:
        print("Hecho")
    return render_template("index.html")

@init.route("/probar")
def probar():
    print(get_register())
    return "nada"

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

