
from flask import render_template, request,send_from_directory,Blueprint, url_for,redirect
from fixtures.utils import get_register,insert_preserts
from aplication import app
from aplication.models.database import Presert
from aplication import cache
from flask import render_template


init = Blueprint('/',__name__)

@init.app_errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

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

@init.route('/image/binarization')
def image_binarization():
    return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'image_binarization.jpg')

@init.route('/prebinarization',methods=["POST"])
def prebinarization():
    message=None
    total_images=Presert.query.all()
    if request.method == "POST":
        print(request.form.getlist('mycheckbox'))
        if len(request.form.getlist('mycheckbox'))==1:
            #El valor entregado sera el id del presert
            #Se consulta el presert para obtener los datos y enviarlo tambien al template para  mostrarlo 
            #para la binarización de la imagen necesito enviar la foto la get_register() para encontrar la imagen
            #necesito crear un methodo que me muestre la imagen binarizada
            return f"Done {request.form.getlist('mycheckbox')}"
        else:
            if  len(request.form.getlist('mycheckbox'))==0:
                message = "No ha seleccionado alguna opción"
            
            if len(request.form.getlist('mycheckbox')) >0:
                message ="Solo puede selecionar una opción"
            return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None, message=message)
    
    return render_template("index.html",imagine=get_file(),preserts=total_images)

