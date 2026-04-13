[README.md](https://github.com/user-attachments/files/26675968/README.md)
# 📚 Biblioteca Popular La Palabra

## Descripción
Sistema de gestión para la Biblioteca Popular La Palabra. Permite registrar y controlar el catálogo de materiales, gestionar socios, registrar préstamos y devoluciones, y generar reportes de uso. Reemplaza el registro manual en cuaderno físico por un sistema digital organizado.

---

## Módulos del Sistema

- **Módulo de Login** — Autenticación de usuarios con usuario y contraseña.
- **Módulo de Categorías** — Gestión de las categorías bibliográficas.
- **Módulo de Autores** — Registro y administración de autores.
- **Módulo de Materiales** — Catálogo de libros, revistas y DVDs con su estado y categoría.
- **Módulo de Autores por Material** — Asociación de autores a materiales (relación muchos a muchos).
- **Módulo de Socios** — Registro de socios con sus datos personales.
- **Módulo de Préstamos** — Registro de préstamos y devoluciones con validación de reglas de negocio.
- **Módulo de Reportes** — Consultas de préstamos activos, vencidos y materiales más prestados.

---

## Herramientas Usadas

| Herramienta | Descripción |
|---|---|
| Python 3.8+ | Lenguaje de programación principal |
| Tkinter | Librería para la interfaz gráfica de escritorio |
| MySQL | Motor de base de datos relacional |
| mysql-connector-python | Conector para comunicar Python con MySQL |

---

## Arquitectura

El proyecto usa arquitectura **MVC (Modelo - Vista - Controlador)** implementada con funciones:

```
proyecto/
│
├── config/
│   └── db.py               # Conexión a la base de datos
│
├── models/                 # Modelo — consultas SQL
│   ├── usuario_model.py
│   ├── categoria_model.py
│   ├── autor_model.py
│   ├── material_model.py
│   ├── material_autor_model.py
│   ├── socio_model.py
│   ├── prestamo_model.py
│   └── reporte_model.py
│
├── controllers/            # Controlador — lógica y validaciones
│   ├── usuario_controller.py
│   ├── categoria_controller.py
│   ├── autor_controller.py
│   ├── material_controller.py
│   ├── material_autor_controller.py
│   ├── socio_controller.py
│   ├── prestamo_controller.py
│   └── reporte_controller.py
│
├── views/                  # Vista — ventanas e interfaces
│   ├── usuario_view.py
│   ├── categoria_view.py
│   ├── autor_view.py
│   ├── material_view.py
│   ├── material_autor_view.py
│   ├── socio_view.py
│   ├── prestamo_view.py
│   └── reporte_view.py
│
└── main.py                 # Punto de arranque del programa
```

---

## Cómo ejecutar el proyecto

1. Clona o descarga el repositorio.
2. Instala el conector de MySQL:
```
pip install mysql-connector-python
```
3. Crea la base de datos en MySQL usando el script SQL incluido.
4. Configura los datos de conexión en `config/db.py`.
5. Ejecuta el programa:
```
python main.py
```

---
## Autor

**Sheyla Geliz**
