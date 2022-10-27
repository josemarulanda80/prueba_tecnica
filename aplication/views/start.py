


from scipy.fftpack import ifftn
from aplication import db
from flask import render_template,abort, request,send_from_directory,Blueprint, url_for,redirect
from fixtures.utils import get_register,insert_preserts
from aplication import app
from aplication.models.database import Presert
from aplication import cache

init = Blueprint('/',__name__)

cache.clear()
@init.route("/")

def index():
    
    total_images=Presert.query.all()
    binarization=None
    print("Holo")
    print(total_images)
    if len(total_images) == 0: 
            insert_preserts()
            
            return url_for('index')
    else:
        return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=binarization,message=None)
    


@init.route('/img',methods=["GET"])

def get_file():
    name_file=get_register()
  
    print(name_file)
    if name_file != "Error: Not conexion":
        if name_file >0 and name_file <5:
            return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'{str(name_file)}.jpg')
        else: 
            return None
    return None

@init.route('/prebinarization',methods=["POST"])
def prebinarization():
    message=None
    total_images=Presert.query.all()
    if request.method == "POST":
        print(request.form.getlist('mycheckbox'))
        if len(request.form.getlist('mycheckbox'))==1:
            return f"Done {request.form.getlist('mycheckbox')}"
        else:
            if  len(request.form.getlist('mycheckbox'))==0:
                message = "No ha seleccionado alguna opción"
            
            if len(request.form.getlist('mycheckbox')) >0:
                message ="Solo puede selecionar una opción"
            return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None, message=message)
    
    return render_template("index.html",imagine=get_file(),preserts=total_images)