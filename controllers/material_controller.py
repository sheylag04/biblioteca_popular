from models.material_model import(
    obtener_materiales,guardar_material,actualizar_material,eliminar_material)
from models.categoria_model import obtener_categorias

def obte_materiales():
    return obtener_materiales()

def obte_categorias():
    # esta funcion la usamos para llenar el combobox
    return obtener_categorias()

def nuevo_material(titulo, id_categoria, estado_material):
    if titulo.strip() == "":
        return "vacio"
    if id_categoria is None:
        return "sin_categoria"
    return guardar_material(titulo, id_categoria, estado_material)

def actu_material(id_material, titulo, id_categoria, estado_material):
    if titulo.strip() == "":
        return "vacio"
    if id_material is None:
        return "sin_seleccion"
    if id_categoria is None:
        return "sin_categoria"
    return actualizar_material(id_material, titulo, id_categoria, estado_material)

def elimi_material(id_material):
    if id_material is None:
        return "sin_seleccion"
    return eliminar_material(id_material)

