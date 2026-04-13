from config.db import get_connection

def obtener_prestamos():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    # usamos JOIN para ver el nombre del socio y el titulo del material
    sql = """
        SELECT p.id_prestamo, s.nombre as socio, m.titulo as material,
               p.fecha_prestamo, p.fecha_limite, p.fecha_devolucion
        FROM prestamo p
        JOIN socio s ON p.id_socio = s.id_socio
        JOIN material m ON p.id_material = m.id_material
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def guardar_prestamo(id_socio, id_material, fecha_prestamo, fecha_limite):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = """INSERT INTO prestamo (id_socio, id_material, fecha_prestamo, fecha_limite)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (id_socio, id_material, fecha_prestamo, fecha_limite))
    conexion.commit()
    conexion.close()
    return True

def registrar_devolucion(id_prestamo, fecha_devolucion):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "UPDATE prestamo SET fecha_devolucion=%s WHERE id_prestamo=%s"
    cursor.execute(sql, (fecha_devolucion, id_prestamo))
    conexion.commit()
    conexion.close()
    return True

# --- VALIDACIONES DE NEGOCIO ---

def material_esta_prestado(id_material):
    # verifica si el material ya esta prestado (no tiene fecha de devolucion)
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "SELECT * FROM prestamo WHERE id_material=%s AND fecha_devolucion IS NULL"
    cursor.execute(sql, (id_material,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None  # si encontro algo, esta prestado

def socio_tiene_prestamos_vencidos(id_socio):
    # verifica si el socio tiene prestamos vencidos sin devolver
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = """SELECT * FROM prestamo 
             WHERE id_socio=%s AND fecha_devolucion IS NULL 
             AND fecha_limite < CURDATE()"""
    cursor.execute(sql, (id_socio,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None

def socio_cantidad_prestamos(id_socio):
    # cuenta cuantos prestamos activos tiene el socio
    conexion = get_connection()
    if conexion is None:
        return 0
    cursor = conexion.cursor()
    sql = "SELECT COUNT(*) FROM prestamo WHERE id_socio=%s AND fecha_devolucion IS NULL"
    cursor.execute(sql, (id_socio,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado[0]  # retorna el numero

def eliminar_prestamo(id_prestamo):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM prestamo WHERE id_prestamo=%s", (id_prestamo,))
    conexion.commit()
    conexion.close()
    return True