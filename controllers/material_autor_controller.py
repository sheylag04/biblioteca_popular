# controllers/material_autor_controller.py
from models import material_autor_model
from models import material_model
from models import autor_model

def obte_asociaciones():
    return material_autor_model.obtener_asociaciones()

def obtener_materiales():
    return material_model.obtener_materiales()

def obtener_autores():
    return autor_model.obtener_autores()

def guar_asociacion(id_material, id_autor):
    if id_material is None:
        return "sin_material"
    if id_autor is None:
        return "sin_autor"
    # verificamos que no exista ya esa combinacion
    if material_autor_model.asociacion_existe(id_material, id_autor):
        return "ya_existe"
    return material_autor_model.guardar_asociacion(id_material, id_autor)

def elimi_asociacion(id_material, id_autor):
    if id_material is None or id_autor is None:
        return "sin_seleccion"
    return material_autor_model.eliminar_asociacion(id_material, id_autor)