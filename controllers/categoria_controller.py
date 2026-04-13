from models.categoria_model import (
    obtener_categorias, guardar_categoria,actualizar_categoria,eliminar_categoria)

# --- OBTENER TODAS ---
def todas_categorias():
    return obtener_categorias()  # <-- llama al MODELO, no a si misma

# --- GUARDAR ---
def nueva_categoria( nombre):
    # Validamos que el nombre no este vacio
    if nombre.strip() == "":
        return "vacio"
    return guardar_categoria(nombre)

# --- ACTUALIZAR ---
def actu_categoria(id_categoria, nombre):
    if nombre.strip() == "":
        return "vacio"
    if id_categoria is None:
        return "sin_seleccion"
    return actualizar_categoria(id_categoria, nombre)

# --- ELIMINAR ---
def elimi_categoria(id_categoria):
    if id_categoria is None:
        return "sin_seleccion"
    return eliminar_categoria(id_categoria)