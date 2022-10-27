
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


def insert_preserts():
    conexion = get_conexion()
    preserts=["a","b","c","d"]
    values=[10,40,70,90]
    fecha = time.strftime("%y/%m/%d")
    with conexion.cursor() as cursor:
        for j in range(0,4):
            cursor.execute("INSERT INTO preserts(filename,value,created) VALUES (%s,%s,%s)",
                        (preserts[j],values[j],fecha))
    conexion.commit()
    conexion.close()