import mysql.connector

#funcion para conectar a la base de datos
def get_connection():
    try:
       conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sena2025*",
            database="biblioteca_la_palabra"

        )
       return conexion
    except mysql.connector.Error as e:
        print("Error de conexion: " , e)
        return None