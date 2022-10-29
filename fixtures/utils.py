from pymodbus.client.tcp import ModbusTcpClient
import pymysql
import time
from skimage import io, color
from skimage.filters import gaussian
import os
from aplication import app, db
from aplication.models.database import Presert

"""
function to obtain the number sent by the modbus protocol
"""
def get_register():
    try:
        """Host de modbus"""
        client = ModbusTcpClient('127.0.0.1')

        client.connect()
        """
        read registre 
        """
        result = client.read_holding_registers(0, 1)

        client.close()
        return (result.registers[0])
    except:
        return "Error: Not conexion"

"""Conexion database mysqlt"""
def get_conexion():
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='jos84mar19',
                               db='imagenes')
    return conexion

"""insert Preserts by default"""
def insert_preserts():
    conexion = get_conexion()
    preserts = ["opción 1", "opción 2", "opción 3", "opción 4"]
    values = [10, 40, 70, 90]
    fecha = time.strftime("%y/%m/%d")
    with conexion.cursor() as cursor:
        for j in range(0, 4):
            cursor.execute("INSERT INTO preserts(filename,value,created) VALUES (%s,%s,%s)",
                           (preserts[j], values[j], fecha))
    conexion.commit()
    conexion.close()


"""function for image binarization"""
def created_binarization(number, filename):
    img = io.imread(app.config.get('UPLOAD_FOLDER')+str(filename)+".jpg")
    img_gris = color.rgb2gray(img)
    t = number/100
    binary_mask = img_gris < t
    io.imshow(binary_mask, cmap="gray")
    io.imsave(os.path.join(app.config.get('UPLOAD_FOLDER'),
              "image_binarization.jpg"), binary_mask)



"""function to query a presert using the id"""
def get_presert(id):
    presert = Presert.query.filter_by(id=id).first()
    return presert
