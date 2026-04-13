from config.db import get_connection

def prestamos_activos():
    # trae todos los prestamos que no han sido devueltos
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    sql = """
        SELECT p.id_prestamo, s.nombre as socio, m.titulo as material,
               p.fecha_prestamo, p.fecha_limite
        FROM prestamo p
        JOIN socio s ON p.id_socio = s.id_socio
        JOIN material m ON p.id_material = m.id_material
        WHERE p.fecha_devolucion IS NULL
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def prestamos_vencidos():
    # trae prestamos que ya pasaron la fecha limite y no se han devuelto
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    sql = """
        SELECT p.id_prestamo, s.nombre as socio, m.titulo as material,
               p.fecha_prestamo, p.fecha_limite
        FROM prestamo p
        JOIN socio s ON p.id_socio = s.id_socio
        JOIN material m ON p.id_material = m.id_material
        WHERE p.fecha_devolucion IS NULL AND p.fecha_limite < CURDATE()
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def materiales_mas_prestados():
    # cuenta cuantas veces se ha prestado cada material
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    sql = """
        SELECT m.titulo, COUNT(p.id_prestamo) as total_prestamos
        FROM prestamo p
        JOIN material m ON p.id_material = m.id_material
        GROUP BY m.id_material, m.titulo
        ORDER BY total_prestamos DESC
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado