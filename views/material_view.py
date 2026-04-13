import tkinter as tk
from tkinter import messagebox,ttk
from controllers.material_controller import (
    obte_materiales,nuevo_material,actu_material,elimi_material,obte_categorias)

id_seleccionado = None
# esta lista guarda las categorias para saber el id de la seleccionada en el combobox
lista_categorias = []

def abrir_materiales(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Gestión de Materiales")
    ventana.geometry("900x600")

    tk.Label(ventana, text="📖Materiales", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    tk.Label(frame_form, text="Título:").grid(row=0, column=0, padx=5, pady=5)
    entry_titulo = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_titulo.grid(row=0, column=1, padx=5, pady=5)

    # Combobox de categorias
    tk.Label(frame_form, text="Categoría:").grid(row=1, column=0, padx=5, pady=5)
    combo_categoria = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_categoria.grid(row=1, column=1, padx=5, pady=5)

    # Combobox de estado (valores fijos)
    tk.Label(frame_form, text="Estado:").grid(row=2, column=0, padx=5, pady=5)
    combo_estado = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_estado["values"] = ["disponible", "prestado", "baja"]
    combo_estado.grid(row=2, column=1, padx=5, pady=5)

    # --- FUNCION PARA LLENAR EL COMBOBOX DE CATEGORIAS ---
    def cargar_categorias():
        global lista_categorias
        lista_categorias = obte_categorias()
        # al combobox solo le mostramos los nombres
        nombres = [c["nombre"] for c in lista_categorias]
        combo_categoria["values"] = nombres

    # --- FUNCIONES ---
    def limpiar_campos():
        global id_seleccionado
        id_seleccionado = None
        entry_titulo.delete(0, tk.END)
        combo_categoria.set("")  # limpia el combobox
        combo_estado.set("")

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        materiales = obte_materiales()
        for m in materiales:
            tabla.insert("", tk.END, values=(
                m["id_material"], m["titulo"], m["categoria"], m["estado_material"]
            ))

    def al_seleccionar(_):
        global id_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_seleccionado = fila[0]
            entry_titulo.delete(0, tk.END)
            entry_titulo.insert(0, fila[1])
            # ponemos la categoria en el combobox
            combo_categoria.set(fila[2])
            # ponemos el estado en el combobox
            combo_estado.set(fila[3])

    def obtener_id_categoria():
        # buscamos el id de la categoria seleccionada en el combobox
        nombre_seleccionado = combo_categoria.get()
        for c in lista_categorias:
            if c["nombre"] == nombre_seleccionado:
                return c["id_categoria"]
        return None

    def guardar():
        titulo = entry_titulo.get()
        id_categoria = obtener_id_categoria()
        estado = combo_estado.get()
        resultado = nuevo_material(titulo, id_categoria, estado)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "El título es obligatorio")
        elif resultado == "sin_categoria":
            messagebox.showwarning("Atención", "Selecciona una categoría")
        else:
            messagebox.showinfo("Éxito", "Material guardado correctamente")
            limpiar_campos()
            cargar_tabla()

    def actualizar():
        global id_seleccionado
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un material de la tabla")
            return
        titulo = entry_titulo.get()
        id_categoria = obtener_id_categoria()
        estado = combo_estado.get()
        resultado = actu_material(id_seleccionado, titulo, id_categoria, estado)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "El título es obligatorio")
        elif resultado == "sin_categoria":
            messagebox.showwarning("Atención", "Selecciona una categoría")
        else:
            messagebox.showinfo("Éxito", "Material actualizado correctamente")
            limpiar_campos()
            cargar_tabla()

    def eliminar():
        global id_seleccionado
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un material de la tabla")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este material?")
        if confirmar:
            elimi_material(id_seleccionado)
            messagebox.showinfo("Éxito", "Material eliminado")
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

    tabla = ttk.Treeview(frame_tabla, columns=("col1","col2","col3","col4"), show="headings")
    tabla.heading("col1", text="ID")
    tabla.heading("col2", text="Título")
    tabla.heading("col3", text="Categoría")
    tabla.heading("col4", text="Estado")
    tabla.column("col1", width=40)
    tabla.column("col2", width=200)
    tabla.column("col3", width=150)
    tabla.column("col4", width=100)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    # cargamos categorias y tabla al abrir la ventana
    cargar_categorias()
    cargar_tabla()