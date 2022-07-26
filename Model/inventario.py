import psycopg2
from DataBase.conexion_db import DataBase

def readInv():
    conexion = DataBase.conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM inventario;")
            invetario = cursor.fetchall()
            if invetario:
                return invetario
    except psycopg2.Error as e:
        print("Ocurrio un error: ",e)
    finally:
        conexion.close()
            
def createProduct(producto,precio,cantidad):
    conexion = DataBase.conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO inventario (producto,precio,cantidad,cantidadinicial) VALUES ('"+str(producto)+"',"+str(precio)+","+str(cantidad)+","+str(cantidad)+";")
        conexion.commit()
        return True
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        conexion.close()
        
def updateProduct(prodcuto,precio,cantidad):
    conexion = DataBase.conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE inventario SET producto = '"+str(prodcuto)+
                            "', precio = "+str(precio)+
                            ", cantidad = "+str(cantidad)+";")
        conexion.commit()
        return True
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        conexion.close()