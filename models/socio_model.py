from config.db import get_connection

def obtener_socios():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM socio")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def guardar_socio(nombre,direccion,telefono,email,fecha_inscripcion,estado_socio):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "insert into socio (nombre,direccion,telefono,email,fecha_inscripcion,estado_socio)" \
    "values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(nombre,direccion,telefono,email,fecha_inscripcion,estado_socio))
    conexion.commit()
    conexion.close()
    return True

def actualizar_socio(id_socio, nombre, direccion, telefono, email, fecha_inscripcion, estado_socio):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = """UPDATE socio SET nombre=%s, direccion=%s, telefono=%s,
             email=%s, fecha_inscripcion=%s, estado_socio=%s WHERE id_socio=%s"""
    cursor.execute(sql, (nombre, direccion, telefono, email, fecha_inscripcion, estado_socio, id_socio))
    conexion.commit()
    conexion.close()
    return True

def eliminar_socio(id_socio):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM socio WHERE id_socio=%s", (id_socio,))
    conexion.commit()
    conexion.close()
    return True