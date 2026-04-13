import tkinter as tk
from tkinter import messagebox, ttk

from controllers import prestamo_controller

id_prestamo_seleccionado = None
lista_socios = []
lista_materiales = []

def abrir_prestamos(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Gestión de Préstamos")
    ventana.geometry("900x600")

    tk.Label(ventana, text="🔖 Préstamos", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    # combobox de socios
    tk.Label(frame_form, text="Socio:").grid(row=0, column=0, padx=5, pady=5)
    combo_socio = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_socio.grid(row=0, column=1, padx=5, pady=5)

    # combobox de materiales
    tk.Label(frame_form, text="Material:").grid(row=1, column=0, padx=5, pady=5)
    combo_material = ttk.Combobox(frame_form, width=28, state="readonly",background="#DADFE4")
    combo_material.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Fecha Préstamo (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
    entry_fecha_prestamo = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_fecha_prestamo.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Fecha Límite (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
    entry_fecha_limite = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_fecha_limite.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Fecha Devolución (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5)
    entry_fecha_devolucion = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_fecha_devolucion.grid(row=4, column=1, padx=5, pady=5)

    # --- FUNCIONES ---
    def cargar_combos():
        global lista_socios, lista_materiales
        lista_socios = prestamo_controller.obtener_socios()
        lista_materiales = prestamo_controller.obtener_materiales()
        combo_socio["values"] = [s["nombre"] for s in lista_socios]
        combo_material["values"] = [m["titulo"] for m in lista_materiales]

    def eliminar():
        global id_prestamo_seleccionado
        if id_prestamo_seleccionado is None:
           messagebox.showwarning("Atención", "Selecciona un préstamo de la tabla")
           return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este préstamo?")
        if confirmar:
           prestamo_controller.eliminar_prestamo(id_prestamo_seleccionado)
           messagebox.showinfo("Éxito", "Préstamo eliminado")
           limpiar_campos()
           cargar_tabla()

    def obtener_id_socio():
        nombre = combo_socio.get()
        for s in lista_socios:
            if s["nombre"] == nombre:
                return s["id_socio"]
        return None

    def obtener_id_material():
        titulo = combo_material.get()
        for m in lista_materiales:
            if m["titulo"] == titulo:
                return m["id_material"]
        return None

    def limpiar_campos():
        global id_prestamo_seleccionado
        id_prestamo_seleccionado = None
        combo_socio.set("")
        combo_material.set("")
        entry_fecha_prestamo.delete(0, tk.END)
        entry_fecha_limite.delete(0, tk.END)
        entry_fecha_devolucion.delete(0, tk.END)

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        prestamos = prestamo_controller.obte_prestamos()
        for p in prestamos:
            tabla.insert("", tk.END, values=(
                p["id_prestamo"], p["socio"], p["material"],
                p["fecha_prestamo"], p["fecha_limite"], p["fecha_devolucion"]
            ))

    def al_seleccionar(_):
        global id_prestamo_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_prestamo_seleccionado = fila[0]
            combo_socio.set(fila[1])
            combo_material.set(fila[2])
            entry_fecha_prestamo.delete(0, tk.END)
            entry_fecha_prestamo.insert(0, fila[3])
            entry_fecha_limite.delete(0, tk.END)
            entry_fecha_limite.insert(0, fila[4])
            entry_fecha_devolucion.delete(0, tk.END)
            # la devolucion puede estar vacia si no se ha devuelto
            if fila[5] != "None" and fila[5] is not None:
                entry_fecha_devolucion.insert(0, fila[5])

    def guardar():
        id_socio    = obtener_id_socio()
        id_material = obtener_id_material()
        fecha_prestamo = entry_fecha_prestamo.get()
        fecha_limite   = entry_fecha_limite.get()

        resultado = prestamo_controller.guar_prestamo(
            id_socio, id_material, fecha_prestamo, fecha_limite)

        if resultado == "sin_socio":
            messagebox.showwarning("Atención", "Selecciona un socio")
        elif resultado == "sin_material":
            messagebox.showwarning("Atención", "Selecciona un material")
        elif resultado == "vacio":
            messagebox.showwarning("Atención", "Las fechas son obligatorias")
        elif resultado == "socio_vencido":
            messagebox.showwarning("Atención", "El socio tiene préstamos vencidos sin devolver")
        elif resultado == "limite_prestamos":
            messagebox.showwarning("Atención", "El socio ya tiene 3 préstamos activos")
        elif resultado == "material_prestado":
            messagebox.showwarning("Atención", "Ese material ya está prestado")
        else:
            messagebox.showinfo("Éxito", "Préstamo registrado correctamente")
            limpiar_campos()
            cargar_tabla()

    def devolver():
        global id_prestamo_seleccionado
        if id_prestamo_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un préstamo de la tabla")
            return
        fecha_devolucion = entry_fecha_devolucion.get()
        resultado = prestamo_controller.registrar_devolucion(
            id_prestamo_seleccionado, fecha_devolucion)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "Escribe la fecha de devolución")
        else:
            messagebox.showinfo("Éxito", "Devolución registrada correctamente")
            limpiar_campos()
            cargar_tabla()

    # --- BOTONES ---
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Nuevo",    width=12, command=limpiar_campos,background="#ACCDF2").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Guardar",  width=12, command=guardar,background="#ACCDF2").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Devolver", width=12, command=devolver,background="#ACCDF2").grid(row=0, column=2, padx=5)
    tk.Button(frame_botones, text="Eliminar", width=12, command=eliminar,background="#ACCDF2").grid(row=0, column=3, padx=5)
    
    # --- TABLA ---
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, fill="both", expand=True)

    tabla = ttk.Treeview(frame_tabla,
                         columns=("col1","col2","col3","col4","col5","col6"),
                         show="headings")
    tabla.heading("col1", text="ID")
    tabla.heading("col2", text="Socio")
    tabla.heading("col3", text="Material")
    tabla.heading("col4", text="Fecha Préstamo")
    tabla.heading("col5", text="Fecha Límite")
    tabla.heading("col6", text="Fecha Devolución")

    tabla.column("col1", width=30)
    tabla.column("col2", width=120)
    tabla.column("col3", width=150)
    tabla.column("col4", width=100)
    tabla.column("col5", width=100)
    tabla.column("col6", width=100)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    cargar_combos()
    cargar_tabla()