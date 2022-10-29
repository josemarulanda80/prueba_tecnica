
from flask import render_template, request,send_from_directory,Blueprint, url_for,redirect,request
from sqlalchemy import values
from fixtures.utils import get_register,insert_preserts,get_presert,created_binarization
from aplication import app,db
from aplication.models.database import Presert
from aplication import cache
from flask import render_template


init = Blueprint('/',__name__)

total_images=Presert.query.all()
@init.app_errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404


@init.route("/")

def index():
    cache.clear()
    total_images=Presert.query.all()
    binarization=None
    if len(total_images) == 0: 
            insert_preserts()
            
            return url_for('index')
    else:
        return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=binarization,message=None)
    


@init.route('/img',methods=["GET"])

def get_file():
    cache.clear()
    name_file=get_register()
    if name_file != "Error: Not conexion":
        if name_file >0 and name_file <5:
            return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'{str(name_file)}.jpg')
        else: 
            return None
    return None

@init.route('/image/binarization')
def image_binarization():
    cache.clear()
    return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'image_binarization.jpg')

@init.route('/prebinarization',methods=["POST"])
def prebinarization():
    cache.clear()
    message=None

    if request.method == "POST":

        if len(request.form.getlist('mycheckbox'))==1:
            presert_selected= get_presert(request.form.getlist('mycheckbox')[0])
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
    cache.clear()
    if request.method == "POST":

        update_presert=get_presert(request.form['id'])
        if request.form['res'] == "update":
           
            if update_presert != None:
               
                if  str(update_presert.value) != str(request.form['value']):
                    update_presert.filename=request.form['name']
                    update_presert.value=request.form['value']
                    db.session.commit()
                    return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None,message=None)
                else:
                     return  render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None,message="No se puede editar por que no hay cambios")
            else:
                 return render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None,message="Error desconocido")
        else:
            
            if str(update_presert.value) != str(request.form['value']):
                new_presert=Presert(filename=request.form['name'],value=request.form['value'])
                db.session.add(new_presert)
                db.session.commit()
                return redirect(url_for('.index'))
            else:
                return  render_template("index.html",imagine=get_file(),preserts=total_images,binarization=None,message="No es posible crear, por que el valor ya existe")
            


@init.route('/deletes/<int:id>')

def delete(id):
    cache.clear()
    delete_presert=Presert.query.filter_by(id=id).first()
    if delete_presert != None:
        db.session.delete(delete_presert)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        return redirect(url_for('.app_errorhandler'))





