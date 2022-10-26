
from asyncio import sleep
from pymodbus.client.tcp import ModbusTcpClient


def get_register():
    try:
        client = ModbusTcpClient('127.0.0.1')
        client.connect()

        # if client.socket == None:
        #     print ("ERROR: Could not connect to")
        #     return "No funciono"
        # print (' Connected.')
        result = client.read_holding_registers(0,1)
        print((result.registers[0]))
        client.close()
        return (result.registers[0])
    except:
        print("Error de conexion")
        return "Horrible"
    




