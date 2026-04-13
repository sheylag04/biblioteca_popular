
import tkinter as tk
from tkinter import messagebox
from controllers.usuario_controller import login
from views import categoria_view
from views import autor_view
from views import socio_view
from views import material_view
from views import prestamo_view
from views import material_autor_view
from views import reporte_view



 #-----------------------------------------------
# VENTANA DE LOGIN
# -----------------------------------------------
def abrir_login():
    ventana = tk.Tk()  # esta es la ventana raiz, solo se crea UNA vez
    ventana.title("Biblioteca Popular La Palabra - Login")
    ventana.geometry("600x300")
    ventana.resizable(False, False)

   
    tk.Label(ventana, text="📚Biblioteca Popular la Palabra", font=("Arial", 26, "bold")).pack(pady=15)
    
    tk.Label(ventana, text="Usuario:").pack()
    entry_usuario = tk.Entry(ventana, width=30,background="#DADFE4")
    entry_usuario.pack(pady=5)

    tk.Label(ventana, text="Contrasena:").pack()
    entry_contrasena = tk.Entry(ventana, width=30, show="*",background="#DADFE4")
    entry_contrasena.pack(pady=5)

    def al_hacer_clic_entrar():
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()

        resultado = login(usuario, contrasena, ventana)

        if resultado == "ok":
            messagebox.showinfo("bienvenido al sistema","biblioteca popular")
            ventana.withdraw()              # ocultamos el login
            abrir_menu_principal(ventana)   # le pasamos ventana como raiz

        elif resultado == "vacio":
            messagebox.showwarning("Atención", "Por favor completa todos los campos")

        elif resultado == "error":
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana, text="Entrar", width=15, command=al_hacer_clic_entrar,background="#ACCDF2").pack(pady=15)

    ventana.mainloop()  # solo hay UN mainloop en todo el programa

# -----------------------------------------------
# VENTANA MENU PRINCIPAL
# -----------------------------------------------
def abrir_menu_principal(ventana_raiz):  # <-- recibe ventana_raiz como parametro
    menu = tk.Toplevel(ventana_raiz)  # <-- Toplevel, NO tk.Tk()
    menu.title("Biblioteca Popular La Palabra - Menú Principal")
    menu.geometry("900x600")

    # Si cierran el menu, se cierra todo el programa
    menu.protocol("WM_DELETE_WINDOW", ventana_raiz.destroy)

    tk.Label(menu, text="Menú Principal", font=("Arial", 26, "bold")).pack(pady=20)

    
    # Le pasamos ventana_raiz a cada modulo para que puedan abrir Toplevel

    # --- Botones de cada modulo ---
    tk.Button(menu, text="Categorías", width=20,
        command=lambda: categoria_view.abrir_categorias(ventana_raiz),background="#ACCDF2").pack(pady=5)
    
    tk.Button(menu, text="Autores", width=20,
    command=lambda: autor_view.abrir_autores(ventana_raiz),background="#ACCDF2").pack(pady=5)

    tk.Button(menu, text="Materiales", width=20,
    command=lambda: material_view.abrir_materiales(ventana_raiz),background="#ACCDF2").pack(pady=5)

    tk.Button(menu, text="Socios", width=20,
    command=lambda: socio_view.abrir_socios(ventana_raiz),background="#ACCDF2").pack(pady=5)

    tk.Button(menu, text="Préstamos", width=20,
    command=lambda: prestamo_view.abrir_prestamos(ventana_raiz),background="#ACCDF2").pack(pady=5)

    tk.Button(menu, text="Autores por Material", width=20,
    command=lambda: material_autor_view.abrir_material_autor(ventana_raiz),background="#ACCDF2").pack(pady=5)

    tk.Button(menu, text="Reportes", width=20,
    command=lambda: reporte_view.abrir_reportes(ventana_raiz),background="#ACCDF2").pack(pady=5)