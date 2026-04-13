from config.db import get_connection

def verificar_usuario(usuario, contrasena):
    # Esta funcion busca en la BD si el usuario y contraseña existen
    
    conexion = get_connection ()  # abrimos la conexion
    
    if conexion is None:
        return None  # si no hay conexion, retornamos None
    
    cursor = conexion.cursor(dictionary=True)  # dictionary=True nos da los datos como diccionario
    
    # La consulta busca un usuario que coincida con usuario Y contraseña
    sql = "SELECT * FROM usuario WHERE usuario = %s AND contrasena = %s"
    valores = (usuario, contrasena)
    
    cursor.execute(sql, valores)  # ejecutamos la consulta
    resultado = cursor.fetchone()  # fetchone trae solo 1 resultado
    
    conexion.close()  # cerramos la conexion
    
    return resultado  # retorna el usuario encontrado, o None si no existe