
from pymodbus.client.tcp import ModbusTcpClient
import pymysql
import time


def get_register():
    try:
        client = ModbusTcpClient('127.0.0.1')
        client.connect()
        result = client.read_holding_registers(0,1)
        client.close()
        return (result.registers[0])
    except:
        return "Error: Not conexion"
    


def get_conexion():
    conexion=pymysql.connect(host='localhost',
                                user='root',
                                password='jos84mar19',
                                db='imagenes')

    return conexion
def insert_images():
    conexion = get_conexion()
    images=["1.jpg","2.jpg","3.jpg","4.jpg"]
    fecha = time.strftime("%y/%m/%d")
    with conexion.cursor() as cursor:

        for i in images:
            cursor.execute("INSERT INTO images(filename,created) VALUES (%s,%s)",
                       (i,fecha))
    conexion.commit()
    conexion.close()
    conexion = get_conexion()
    insert_preserts()


def insert_preserts():
    conexion = get_conexion()
    preserts=[0.1,0.4,0.7,0.9]
    fecha = time.strftime("%y/%m/%d")
    with conexion.cursor() as cursor:
        for j in range(1,5):
            for i in preserts:
                cursor.execute("INSERT INTO preserts(img,value,created) VALUES (%s,%s,%s)",
                        (j,i,fecha))
    conexion.commit()
    conexion.close()