from aplication import db
from flask import render_template,abort,send_from_directory,Blueprint
from fixtures.utils import get_register
from aplication import app
init = Blueprint('/',__name__)

@init.route("/")
def index():
#     images=["1.jpg","2.jpg","3.jpg","4.jpg"]
   
#     new_image=Image(filename=images[0])
#     db.session.add(new_image)
#     db.session.commit()
    
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

