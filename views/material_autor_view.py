import tkinter as tk
from tkinter import messagebox, ttk
from controllers import material_autor_controller

# guardamos el material e id autor de la fila seleccionada
id_material_seleccionado = None
id_autor_seleccionado = None
lista_materiales = []
lista_autores = []

def abrir_material_autor(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Asociar Autores a Materiales")
    ventana.geometry("900x600")

    tk.Label(ventana, text="🔗Autores por Material", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    # combobox de materiales
    tk.Label(frame_form, text="Material:").grid(row=0, column=0, padx=5, pady=5)
    combo_material = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_material.grid(row=0, column=1, padx=5, pady=5)

    # combobox de autores
    tk.Label(frame_form, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
    combo_autor = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_autor.grid(row=1, column=1, padx=5, pady=5)

    # --- FUNCIONES ---
    def cargar_combos():
        global lista_materiales, lista_autores
        lista_materiales = material_autor_controller.obtener_materiales()
        lista_autores = material_autor_controller.obtener_autores()
        combo_material["values"] = [m["titulo"] for m in lista_materiales]
        combo_autor["values"] = [a["nombre"] for a in lista_autores]

    def obtener_id_material():
        titulo = combo_material.get()
        for m in lista_materiales:
            if m["titulo"] == titulo:
                return m["id_material"]
        return None

    def obtener_id_autor():
        nombre = combo_autor.get()
        for a in lista_autores:
            if a["nombre"] == nombre:
                return a["id_autor"]
        return None

    def limpiar_campos():
        global id_material_seleccionado, id_autor_seleccionado
        id_material_seleccionado = None
        id_autor_seleccionado = None
        combo_material.set("")
        combo_autor.set("")

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        asociaciones = material_autor_controller.obte_asociaciones()
        for a in asociaciones:
            tabla.insert("", tk.END, values=(
                a["id_material"], a["titulo"], a["id_autor"], a["autor"]
            ))

    def al_seleccionar(_):
        global id_material_seleccionado, id_autor_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_material_seleccionado = fila[0]
            id_autor_seleccionado = fila[2]
            combo_material.set(fila[1])
            combo_autor.set(fila[3])

    def guardar():
        id_material = obtener_id_material()
        id_autor = obtener_id_autor()
        resultado = material_autor_controller.guar_asociacion(id_material, id_autor)
        if resultado == "sin_material":
            messagebox.showwarning("Atención", "Selecciona un material")
        elif resultado == "sin_autor":
            messagebox.showwarning("Atención", "Selecciona un autor")
        elif resultado == "ya_existe":
            messagebox.showwarning("Atención", "Ese autor ya está asociado a ese material")
        else:
            messagebox.showinfo("Éxito", "Asociación guardada correctamente")
            limpiar_campos()
            cargar_tabla()

    def eliminar():
        global id_material_seleccionado, id_autor_seleccionado
        if id_material_seleccionado is None or id_autor_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona una asociación de la tabla")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta asociación?")
        if confirmar:
            material_autor_controller.eliminar_asociacion(
                id_material_seleccionado, id_autor_seleccionado)
            messagebox.showinfo("Éxito", "Asociación eliminada")
            limpiar_campos()
            cargar_tabla()

    # --- BOTONES ---
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Nuevo",   width=12, command=limpiar_campos,background="#ACCDF2").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Guardar", width=12, command=guardar,background="#ACCDF2").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Eliminar",width=12, command=eliminar,background="#ACCDF2").grid(row=0, column=2, padx=5)

    # --- TABLA ---
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, fill="both", expand=True)

    tabla = ttk.Treeview(frame_tabla,
                         columns=("col1","col2","col3","col4"),
                         show="headings")
    tabla.heading("col1", text="ID Material")
    tabla.heading("col2", text="Título")
    tabla.heading("col3", text="ID Autor")
    tabla.heading("col4", text="Autor")

    tabla.column("col1", width=80)
    tabla.column("col2", width=200)
    tabla.column("col3", width=80)
    tabla.column("col4", width=180)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    cargar_combos()
    cargar_tabla()