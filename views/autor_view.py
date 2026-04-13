from controllers.autor_controller import(
    obte_autores,nuevo_autor,actu_autor,elimi_autor)

import tkinter as tk
from tkinter import messagebox, ttk


id_seleccionado = None

def abrir_autores(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Gestión de Autores")
    ventana.geometry("900x600")

    tk.Label(ventana, text="✍️ Autores", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Nacionalidad:").grid(row=1, column=0, padx=5, pady=5)
    entry_nacionalidad = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_nacionalidad.grid(row=1, column=1, padx=5, pady=5)


     # --- FUNCIONES ---
    def limpiar_campos():
        global id_seleccionado
        id_seleccionado = None
        entry_nombre.delete(0, tk.END)
        entry_nacionalidad.delete(0, tk.END)

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        autores = obte_autores()
        for a in autores:
            tabla.insert("", tk.END, values=(a["id_autor"], a["nombre"], a["nacionalidad"]))

    def al_seleccionar(_):
        global id_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_seleccionado = fila[0]
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, fila[1])
            entry_nacionalidad.delete(0, tk.END)
            entry_nacionalidad.insert(0, fila[2])

    def guardar():
        nombre = entry_nombre.get()
        nacionalidad = entry_nacionalidad.get()
        resultado = nuevo_autor(nombre, nacionalidad)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
        else:
            messagebox.showinfo("Éxito", "Autor guardado correctamente")
            limpiar_campos()
            cargar_tabla()

    def actualizar():
        global id_seleccionado
        nombre = entry_nombre.get()
        nacionalidad = entry_nacionalidad.get()
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un autor de la tabla")
            return
        if nombre.strip() == "":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
            return
        actu_autor(id_seleccionado, nombre, nacionalidad)
        messagebox.showinfo("Éxito", "Autor actualizado correctamente")
        limpiar_campos()
        cargar_tabla()
    
    def eliminar():
        global id_seleccionado
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un autor de la tabla")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este autor?")
        if confirmar:
            elimi_autor(id_seleccionado)
            messagebox.showinfo("Éxito", "Autor eliminado")
            limpiar_campos()
            cargar_tabla()
    

    # --- BOTONES ---
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Nuevo",      width=12, command=limpiar_campos,background="#ACCDF2").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Guardar",    width=12, command=guardar,background="#ACCDF2").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Actualizar", width=12, command=actualizar,background="#ACCDF2").grid(row=0, column=2, padx=5)
    tk.Button(frame_botones, text="Eliminar",   width=12, command=eliminar,background="#ACCDF2").grid(row=0, column=3, padx=5)

    # --- TABLA ---
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, fill="both", expand=True)

    tabla = ttk.Treeview(frame_tabla, columns=("col1", "col2", "col3"), show="headings")
    tabla.heading("col1", text="ID")
    tabla.heading("col2", text="Nombre")
    tabla.heading("col3", text="Nacionalidad")
    tabla.column("col1", width=50)
    tabla.column("col2", width=200)
    tabla.column("col3", width=180)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    cargar_tabla()