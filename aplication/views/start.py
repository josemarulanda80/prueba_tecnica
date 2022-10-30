from flask import render_template, request,send_from_directory,Blueprint, url_for,redirect,request
from sqlalchemy import values
from fixtures.utils import get_register,insert_preserts,get_presert,created_binarization
from aplication import app,db
from aplication.models.database import Presert

from flask import render_template


bp = Blueprint('/',__name__)


@bp.app_errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

"""application startup endpoint that renders the main application components"""
@bp.route("/")
def index():
    binarization=None
    total_images=Presert.query.all()
    if len(total_images) == 0: 
            insert_preserts()
            
            return url_for('index')
    else:
     
        return render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=binarization,message=None,imagen=get_register())

"""endpoint to display the image"""
@bp.route('/img/<int:name>',methods=["GET"])
def get_file(name):
    """get number of modbu"""
    g=name
    if g != "Error: Not conexion":
        if g >0 and g <5:
            return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'{str(g)}.jpg')
        else: 
            return None
    return None

@bp.route('/image/binarization')
def image_binarization():
    return send_from_directory(app.config.get('UPLOAD_FOLDER'),path=f'image_binarization.jpg')

"""Function to be able to validate the form for presert"""
@bp.route('/prebinarization',methods=["POST"])
def prebinarization():
    message=None
    if request.method == "POST":
        """check that a presert is selected"""
        if len(request.form.getlist('mycheckbox'))==1:
            presert_selected= get_presert(request.form.getlist('mycheckbox')[0])
            created_binarization(presert_selected.value,get_register())
            total_preserts=Presert.query.all()
            return render_template("index.html",imagine=get_file(get_register()),preserts=total_preserts,binarization=True, message=None, presert=presert_selected, imagen=get_register())
        else:
            """Error presert selected"""
            total_images=Presert.query.all()
            if  len(request.form.getlist('mycheckbox'))==0:
                message = "No ha seleccionado alguna opción"
            if len(request.form.getlist('mycheckbox')) >0:
                message ="Solo puede selecionar una opción"
            return render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=None, message=message,imagen=get_register())

@bp.route('/presets',methods=["POST"])
def presets():
    if request.method == "POST":

        update_presert=get_presert(request.form['id'])
        if request.form['res'] == "update":
           
            if update_presert != None:
                total_images=Presert.query.all()
                if  str(update_presert.value) != str(request.form['value']):
                    update_presert.filename=request.form['name']
                    update_presert.value=request.form['value']
                    db.session.commit()
                    return render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=None,message=None,imagen=get_register())
                else:
                     return  render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=None,message="No se puede editar por que el value ya esta en la base datos",imagen=get_register())
            else:
                 return render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=None,message="Error desconocido",imagen=get_register())
        else:
            total_images=Presert.query.all()
            if str(update_presert.value) != str(request.form['value']):
                new_presert=Presert(filename=request.form['name'],value=request.form['value'])
                db.session.add(new_presert)
                db.session.commit()
                return redirect(url_for('.index'))
            else:
                return  render_template("index.html",imagine=get_file(get_register()),preserts=total_images,binarization=None,message="No es posible crear, por que el valor ya existe",imagen=get_register())
            


@bp.route('/deletes/<int:id>')

def delete(id):
    delete_presert=Presert.query.filter_by(id=id).first()
    if delete_presert != None:
        db.session.delete(delete_presert)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        return redirect(url_for('.app_errorhandler'))





