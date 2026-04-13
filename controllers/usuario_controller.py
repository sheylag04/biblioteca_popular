from models.usuario_model import verificar_usuario

def login(usuario, contrasena,ventana):
    # Esta funcion se llama cuando el usuario hace clic en "Entrar"
    
    # Primero verificamos que no esten vacios los campos
    if usuario == "" or contrasena == "":
        return "vacio"  # le avisamos a la vista que faltan datos
    
    # Le preguntamos al modelo si ese usuario existe en la BD
    usuario = verificar_usuario(usuario, contrasena)
    
    if usuario:
        return "ok"  # el usuario existe, login exitoso
    else:
        return "error"  # usuario o contraseña incorrectos
    
