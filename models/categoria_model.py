from config.db import get_connection

# --- OBTENER TODAS LAS CATEGORIAS ---
def obtener_categorias():
    conexion = get_connection()
    if conexion is None:
        return []
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categoria")
    resultado = cursor.fetchall()  # fetchall trae todos los registros
    conexion.close()
    return resultado

# --- GUARDAR UNA CATEGORIA NUEVA ---
def guardar_categoria(nombre):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categoria (nombre) VALUES (%s)", (nombre,))
    conexion.commit()
    conexion.close()
    return True

def actualizar_categoria(id_categoria, nombre):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    # SET nombre = el nuevo nombre, WHERE id = el id seleccionado
    cursor.execute("UPDATE categoria SET nombre=%s WHERE id_categoria=%s", (nombre, id_categoria))
    conexion.commit()
    conexion.close()
    return True

# --- ELIMINAR UNA CATEGORIA ---
def eliminar_categoria(id_categoria):
    conexion = get_connection()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    sql = "DELETE FROM categoria WHERE id_categoria=%s"
    cursor.execute(sql, (id_categoria,))  # la coma hace que sea una tupla
    conexion.commit()
    conexion.close()
    return True
