from models import prestamo_model
from models import socio_model
from models import material_model

def obte_prestamos():
    return prestamo_model.obtener_prestamos()

def obtener_socios():
    return socio_model.obtener_socios()

def obtener_materiales():
    return material_model.obtener_materiales()

def guar_prestamo(id_socio, id_material, fecha_prestamo, fecha_limite):
    # validamos que no falten datos
    if id_socio is None:
        return "sin_socio"
    if id_material is None:
        return "sin_material"
    if fecha_prestamo.strip() == "" or fecha_limite.strip() == "":
        return "vacio"

    # regla 1: el socio no puede tener prestamos vencidos
    if prestamo_model.socio_tiene_prestamos_vencidos(id_socio):
        return "socio_vencido"

    # regla 2: el socio no puede tener mas de 3 prestamos activos
    if prestamo_model.socio_cantidad_prestamos(id_socio) >= 3:
        return "limite_prestamos"

    # regla 3: el material no puede estar ya prestado
    if prestamo_model.material_esta_prestado(id_material):
        return "material_prestado"

    return prestamo_model.guardar_prestamo(id_socio, id_material, fecha_prestamo, fecha_limite)

def registrar_devolucion(id_prestamo, fecha_devolucion):
    if id_prestamo is None:
        return "sin_seleccion"
    if fecha_devolucion.strip() == "":
        return "vacio"
    return prestamo_model.registrar_devolucion(id_prestamo, fecha_devolucion)

def eliminar_prestamo(id_prestamo):
    if id_prestamo is None:
        return "sin_seleccion"
    return prestamo_model.eliminar_prestamo(id_prestamo)