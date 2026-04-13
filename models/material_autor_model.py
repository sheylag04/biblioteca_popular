from config.db import get_connection

def obtener_asociaciones():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    # traemos los nombres en vez de los ids con JOIN
    sql = """
        SELECT ma.id_material, m.titulo, ma.id_autor, a.nombre as autor
        FROM material_autor ma
        JOIN material m ON ma.id_material = m.id_material
        JOIN autor a ON ma.id_autor = a.id_autor
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def guardar_asociacion(id_material, id_autor):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "INSERT INTO material_autor (id_material, id_autor) VALUES (%s, %s)"
    cursor.execute(sql, (id_material, id_autor))
    conexion.commit()
    conexion.close()
    return True

def eliminar_asociacion(id_material, id_autor):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "DELETE FROM material_autor WHERE id_material=%s AND id_autor=%s"
    cursor.execute(sql, (id_material, id_autor))
    conexion.commit()
    conexion.close()
    return True

def asociacion_existe(id_material, id_autor):
    # verifica si ya existe esa combinacion para no duplicar
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "SELECT * FROM material_autor WHERE id_material=%s AND id_autor=%s"
    cursor.execute(sql, (id_material, id_autor))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None