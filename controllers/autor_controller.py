from models.autor_model import(
    obtener_autores,guardar_autor,actualizar_autor,eliminar_autor)


def obte_autores():
    return obtener_autores()

def nuevo_autor(nombre, nacionalidad):
    if nombre.strip() == "":
        return "vacio"
    return guardar_autor(nombre, nacionalidad)

def actu_autor(id_autor, nombre, nacionalidad):
    if nombre.strip() == "":
        return "vacio"
    if id_autor is None:
        return "sin_seleccion"
    return actualizar_autor(id_autor, nombre, nacionalidad)

def elimi_autor(id_autor):
    if id_autor is None:
        return "sin_seleccion"
    return eliminar_autor(id_autor)