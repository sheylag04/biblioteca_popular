import tkinter as tk
from tkinter import ttk
from controllers.reportes_controller import mate_mas_prestados,pres_activos,pres_vencidos

def abrir_reportes(ventana_raiz):
    ventana = tk.Toplevel(ventana_raiz)
    ventana.title("Reportes")
    ventana.geometry("900x600")

    tk.Label(ventana, text="📊 Reportes", font=("Arial", 26, "bold")).pack(pady=10)

    # --- BOTONES DE REPORTES ---
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Préstamos Activos",
              width=20, command=lambda: cargar_activos(),background="#ACCDF2").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Préstamos Vencidos",
              width=20, command=lambda: cargar_vencidos(),background="#ACCDF2").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Más Prestados",
              width=20, command=lambda: cargar_mas_prestados(),background="#ACCDF2").grid(row=0, column=2, padx=5)

    # --- TABLA ---
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, fill="both", expand=True)

    # la tabla cambia segun el reporte seleccionado
    tabla = ttk.Treeview(frame_tabla, show="headings")
    tabla.pack(fill="both", expand=True)

    # etiqueta que dice que reporte se esta viendo
    label_titulo = tk.Label(ventana, text="", font=("Arial", 11, "italic"))
    label_titulo.pack()

    # --- FUNCIONES ---
    def limpiar_tabla():
        # borra todo lo que hay en la tabla
        for fila in tabla.get_children():
            tabla.delete(fila)
        # borra las columnas
        tabla["columns"] = []

    def cargar_activos():
        limpiar_tabla()
        label_titulo.config(text="Préstamos Activos (sin devolver)")

        # definimos las columnas para este reporte
        tabla["columns"] = ("col1", "col2", "col3", "col4", "col5")
        tabla.heading("col1", text="ID")
        tabla.heading("col2", text="Socio")
        tabla.heading("col3", text="Material")
        tabla.heading("col4", text="Fecha Préstamo")
        tabla.heading("col5", text="Fecha Límite")
        tabla.column("col1", width=40)
        tabla.column("col2", width=150)
        tabla.column("col3", width=180)
        tabla.column("col4", width=120)
        tabla.column("col5", width=120)

        datos = pres_activos()
        for d in datos:
            tabla.insert("", tk.END, values=(
                d["id_prestamo"], d["socio"], d["material"],
                d["fecha_prestamo"], d["fecha_limite"]
            ))

    def cargar_vencidos():
        limpiar_tabla()
        label_titulo.config(text="Préstamos Vencidos (fecha límite superada)")

        tabla["columns"] = ("col1", "col2", "col3", "col4", "col5")
        tabla.heading("col1", text="ID")
        tabla.heading("col2", text="Socio")
        tabla.heading("col3", text="Material")
        tabla.heading("col4", text="Fecha Préstamo")
        tabla.heading("col5", text="Fecha Límite")
        tabla.column("col1", width=40)
        tabla.column("col2", width=150)
        tabla.column("col3", width=180)
        tabla.column("col4", width=120)
        tabla.column("col5", width=120)

        datos = pres_vencidos()
        for d in datos:
            tabla.insert("", tk.END, values=(
                d["id_prestamo"], d["socio"], d["material"],
                d["fecha_prestamo"], d["fecha_limite"]
            ))

    def cargar_mas_prestados():
        limpiar_tabla()
        label_titulo.config(text="Materiales más prestados")

        tabla["columns"] = ("col1", "col2")
        tabla.heading("col1", text="Material")
        tabla.heading("col2", text="Total Préstamos")
        tabla.column("col1", width=300)
        tabla.column("col2", width=120)

        datos = mate_mas_prestados()
        for d in datos:
            tabla.insert("", tk.END, values=(d["titulo"], d["total_prestamos"]))