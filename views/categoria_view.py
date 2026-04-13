import tkinter as tk
from tkinter import messagebox, ttk
from controllers.categoria_controller import (
    todas_categorias,nueva_categoria,actu_categoria,elimi_categoria)

# Variable global para guardar el id de la categoria seleccionada
id_seleccionado = None

def abrir_categorias(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Gestión de Categorías")
    ventana.geometry("900x600")

    tk.Label(ventana, text="📋Categorías", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    # --- FUNCIONES ---
    def limpiar_campos():
        global id_seleccionado
        id_seleccionado = None
        entry_nombre.delete(0, tk.END)

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        categorias = todas_categorias()
        for c in categorias:
            tabla.insert("", tk.END, values=(c["id_categoria"], c["nombre"]))

    def al_seleccionar(event):
        global id_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_seleccionado = fila[0]  # guardamos el id de la fila seleccionada
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, fila[1])  # mostramos el nombre en el campo

    def guardar():
        nombre = entry_nombre.get()
        resultado = nueva_categoria(nombre)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
        else:
            messagebox.showinfo("Éxito", "Categoría guardada correctamente")
            limpiar_campos()
            cargar_tabla()

    def actualizar():
        global id_seleccionado  # <-- esto es clave, decirle que use la variable global
        nombre = entry_nombre.get()

        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Primero selecciona una categoría de la tabla")
            return

        if nombre.strip() == "":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
            return

        actu_categoria(id_seleccionado, nombre)
        messagebox.showinfo("Éxito", "Categoría actualizada correctamente")
        limpiar_campos()
        cargar_tabla()

    def eliminar():
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona una categoría de la tabla")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta categoría?")
        if confirmar:
            elimi_categoria(id_seleccionado)
            messagebox.showinfo("Éxito", "Categoría eliminada")
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

    tabla = ttk.Treeview(frame_tabla, columns=("col1", "col2"), show="headings")
    tabla.heading("col1", text="ID")
    tabla.heading("col2", text="Nombre")
    tabla.column("col1", width=60)
    tabla.column("col2", width=250)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    cargar_tabla()