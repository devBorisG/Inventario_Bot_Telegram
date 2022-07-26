import psycopg2

class DataBase:
    #BASE DATOS MONTADA EN HEROKU
    def conectar():
        try:
            credenciales = {
                "dbname":"dr34lf02ntp5a",
                "user":"iatqbmjcuwfjyu",
                "password":"5d760e0cb792f0885d61392920cc1aa0a2da04f8f9607e09dc6e60c5fc2b6a98",
                "host":"ec2-54-161-255-125.compute-1.amazonaws.com",
                "port":5432
            }
            conexion = psycopg2.connect(**credenciales)
            return conexion
        except psycopg2.Error as e:
            print("Error al conectar con la base de datos:", e)