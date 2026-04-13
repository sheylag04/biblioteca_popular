import tkinter as tk
from tkinter import messagebox,ttk
from controllers.socio_controller import(
    obte_socios,guar_socio,actu_socio,elimi_socio)

id_seleccionado = None

def abrir_socios(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Gestión de Socios")
    ventana.geometry("900x600")

    tk.Label(ventana, text="👥Socios", font=("Arial", 26, "bold")).pack(pady=10)

    # --- FORMULARIO ---
    frame_form = tk.Frame(ventana)
    frame_form.pack(pady=5)

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Dirección:").grid(row=1, column=0, padx=5, pady=5)
    entry_direccion = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_direccion.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
    entry_telefono = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_telefono.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Email:").grid(row=3, column=0, padx=5, pady=5)
    entry_email = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_email.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Fecha_inscripcion (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5)
    entry_fecha = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_fecha.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Estado_socio").grid(row=5, column=0, padx=5, pady=5)
    entry_estado = tk.Entry(frame_form, width=30,background="#DADFE4")
    entry_estado.grid(row=5, column=1, padx=5, pady=5)

    # --- FUNCIONES ---
    def limpiar_campos():
        global id_seleccionado
        id_seleccionado = None
        entry_nombre.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_fecha.delete(0, tk.END)
        entry_estado.delete(0, tk.END)

    def cargar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        socios = obte_socios()
        for s in socios:
            tabla.insert("", tk.END, values=(
                s["id_socio"], s["nombre"], s["direccion"],
                s["telefono"], s["email"],
                s["fecha_inscripcion"], s["estado_socio"]
            ))

    def al_seleccionar(_):
        global id_seleccionado
        seleccion = tabla.selection()
        if seleccion:
            fila = tabla.item(seleccion[0])["values"]
            id_seleccionado = fila[0]
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, fila[1])
            entry_direccion.delete(0, tk.END)
            entry_direccion.insert(0, fila[2])
            entry_telefono.delete(0, tk.END)
            entry_telefono.insert(0, fila[3])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, fila[4])
            entry_fecha.delete(0, tk.END)
            entry_fecha.insert(0, fila[5])
            entry_estado.delete(0, tk.END)
            entry_estado.insert(0, fila[6])

    def guardar():
        nombre    = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono  = entry_telefono.get()
        email     = entry_email.get()
        fecha     = entry_fecha.get()
        estado    = entry_estado.get()
        resultado = guar_socio(nombre, direccion, telefono, email, fecha, estado)
        if resultado == "vacio":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
        else:
            messagebox.showinfo("Éxito", "Socio guardado correctamente")
            limpiar_campos()
            cargar_tabla()

    def actualizar():
        global id_seleccionado
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un socio de la tabla")
            return
        nombre    = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono  = entry_telefono.get()
        email     = entry_email.get()
        fecha     = entry_fecha.get()
        estado    = entry_estado.get()
        if nombre.strip() == "":
            messagebox.showwarning("Atención", "El nombre es obligatorio")
            return
        actu_socio(id_seleccionado, nombre, direccion, telefono, email, fecha, estado)
        messagebox.showinfo("Éxito", "Socio actualizado correctamente")
        limpiar_campos()
        cargar_tabla()

    def eliminar():
        global id_seleccionado
        if id_seleccionado is None:
            messagebox.showwarning("Atención", "Selecciona un socio de la tabla")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este socio?")
        if confirmar:
            elimi_socio(id_seleccionado)
            messagebox.showinfo("Éxito", "Socio eliminado")
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

    tabla = ttk.Treeview(frame_tabla,
                         columns=("col1","col2","col3","col4","col5","col6","col7"),
                         show="headings")
    tabla.heading("col1", text="ID")
    tabla.heading("col2", text="Nombre")
    tabla.heading("col3", text="Dirección")
    tabla.heading("col4", text="Teléfono")
    tabla.heading("col5", text="Email")
    tabla.heading("col6", text="Fecha_inscripcion")
    tabla.heading("col7", text="Estado_socio")

    tabla.column("col1", width=30)
    tabla.column("col2", width=120)
    tabla.column("col3", width=100)
    tabla.column("col4", width=80)
    tabla.column("col5", width=120)
    tabla.column("col6", width=100)
    tabla.column("col7", width=70)

    tabla.pack(fill="both", expand=True)
    tabla.bind("<<TreeviewSelect>>", al_seleccionar)

    cargar_tabla()

