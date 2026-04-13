
from config.db import get_connection

def obtener_autores():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM autor")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def guardar_autor(nombre, nacionalidad):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO autor (nombre, nacionalidad) VALUES (%s, %s)", (nombre, nacionalidad))
    conexion.commit()
    conexion.close()
    return True

def actualizar_autor(id_autor, nombre, nacionalidad):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("UPDATE autor SET nombre=%s, nacionalidad=%s WHERE id_autor=%s", (nombre, nacionalidad, id_autor))
    conexion.commit()
    conexion.close()
    return True

def eliminar_autor(id_autor):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM autor WHERE id_autor=%s", (id_autor,))
    conexion.commit()
    conexion.close()
    return True