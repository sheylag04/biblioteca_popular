from config.db import get_connection

#obtener material

def obtener_materiales():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    # usamos JOIN para traer el nombre de la categoria en vez del id
    sql = """
        SELECT m.id_material, m.titulo, c.nombre as categoria, m.estado_material
        FROM material m
        JOIN categoria c ON m.id_categoria = c.id_categoria
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def guardar_material(titulo, id_categoria, estado_material):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "INSERT INTO material (titulo, id_categoria, estado_material) VALUES (%s, %s, %s)"
    cursor.execute(sql, (titulo, id_categoria, estado_material))
    conexion.commit()
    conexion.close()
    return True


def actualizar_material(id_material, titulo, id_categoria, estado_material):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "UPDATE material SET titulo=%s, id_categoria=%s, estado_material=%s WHERE id_material=%s"
    cursor.execute(sql, (titulo, id_categoria, estado_material, id_material))
    conexion.commit()
    conexion.close()
    return True

def eliminar_material(id_material):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM material WHERE id_material=%s", (id_material,))
    conexion.commit()
    conexion.close()
    return True