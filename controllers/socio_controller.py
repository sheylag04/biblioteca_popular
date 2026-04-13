from models.socio_model import(
    obtener_socios,guardar_socio,actualizar_socio,eliminar_socio)

def obte_socios():
    return obtener_socios()

def guar_socio(nombre, direccion, telefono, email, fecha_inscripcion, estado_socio):
    if nombre.strip() == "":
        return "vacio"
    return guardar_socio(nombre, direccion, telefono, email, fecha_inscripcion, estado_socio)

def actu_socio(id_socio, nombre, direccion, telefono, email, fecha_inscripcion, estado_socio):
    if nombre.strip() == "":
        return "vacio"
    if id_socio is None:
        return "sin_seleccion"
    return actualizar_socio(id_socio, nombre, direccion, telefono, email, fecha_inscripcion, estado_socio)

def elimi_socio(id_socio):
    if id_socio is None:
        return "sin_seleccion"
    return eliminar_socio(id_socio)