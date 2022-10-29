
from flask import render_template, request,send_from_directory,Blueprint, url_for,redirect,request
from sqlalchemy import values
from fixtures.utils import get_register,insert_preserts,get_presert,created_binarization
from aplication import app,db
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
            presert_selected= get_presert(request.form.getlist('mycheckbox')[0])
            print("Holi")
            print(presert_selected.filename)
            print(presert_selected.value)
            created_binarization(presert_selected.value,get_register())
            return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=True, message=None, presert=presert_selected)
        else:
            if  len(request.form.getlist('mycheckbox'))==0:
                message = "No ha seleccionado alguna opción"
            
            if len(request.form.getlist('mycheckbox')) >0:
                message ="Solo puede selecionar una opción"
            
            return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None, message=message)

@init.route('/presets',methods=["POST"])
def presets():
    
    if request.method == "POST":

        update_presert=get_presert(request.form['id'])
        if request.form['res'] == "update":
           
            if update_presert != None:
               
                if  str(update_presert.value) != str(request.form['value']):
                    update_presert.filename=request.form['name']
                    update_presert.value=request.form['value']
                    db.session.commit()
                    return redirect(url_for('.index'))
                else:
                     return " no se puede editar"
            else:
                 return "no papi"
        else:
            print("Holi2")
            print(Presert.query.filter_by(id=request.form['id']).first())
            print(request.form['value'])
            
            if str(update_presert.value) != str(request.form['value']):
                new_presert=Presert(filename=request.form['name'],value=request.form['value'])
                db.session.add(new_presert)
                db.session.commit()
                return  redirect(url_for('.index'))
            else:
                return  " no se puede crear"
            


@init.route('/deletes/<int:id>')
def delete(id):
    delete_presert=Presert.query.filter_by(id=id).first()
    if delete_presert != None:
        db.session.delete(delete_presert)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        return "Normal"





# Renderizar la pagina para cuando las acciones estan bien
#aplicar flash para mostrar mensajes de error
# Renderizar la pagina para cuando las acciones estan mal