# 🎫 Gestión de tickets en Línea  - Flask + MySQL

Este proyecto permite gestionar cursos en línea donde **técnico** pueden crear tickets, y **usuarios** pueden visualizarlos. Además, los **administradores** pueden gestionar usuarios y roles. Es el Proyecto 6 dentro de una colección de 11 proyectos desarrollados como práctica final.

A continuación, capturas de algunas de la interfaces del front-end del proyecto:

# Login
![image](https://github.com/user-attachments/assets/4c2fdd9e-c5eb-4ecb-aca8-c254bf17fc3a)

# Registro
![image](https://github.com/user-attachments/assets/c1a82aca-b3da-4e5e-8e16-871cb542a228)

# Dashboard
![image](https://github.com/user-attachments/assets/04457312-91c6-4e35-b569-2d4e3c1cef87)

# Lista de usuarios y técnicos registrados
![image](https://github.com/user-attachments/assets/f5299dbe-1e10-4e34-8156-08c88d85755e)

## 🚀 Tecnologías utilizadas

- **Flask** – Framework backend en Python
- **Flask-Login** – Sistema de autenticación
- **MySQL** – Base de datos relacional
- **SQLAlchemy** – ORM para la base de datos
- **Bootstrap 5** – Framework CSS responsivo
- **Jinja2** – Motor de plantillas para HTML

---

## 📂 Estructura del proyecto

| Archivo / Carpeta                                                 | Descripción                                                                |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `create_demo_users.py`                                            | Script para crear usuarios iniciales con roles y contraseñas               |
| `config.py`                                                       | Configuración de Flask (DB URI, claves, etc.)                              |
| `README.md`                                                       | Este archivo de documentación del proyecto                                 |
| `requirements.txt`                                                | Lista de paquetes Python requeridos                                        |
| **`run.py`**                                                      | Punto de entrada para ejecutar el servidor Flask                           |
| `app/__init__.py`                                                 | Inicializa la aplicación Flask y carga la configuración                    |
| `app/models.py`                                                   | Contiene los modelos SQLAlchemy: User, Role, Ticket                         |
| `app/forms.py`                                                    | Formularios de Flask-WTF usados en login, registro, cursos, contraseñas    |
| `app/routes.py`                                                   | Rutas principales del proyecto (dashboard, tickets, cambiar contraseña)     |
| `app/auth_routes.py`                                              | Rutas para autenticación (login, registro, logout)                         |
| `app/templates/layout.html`                                       | Plantilla base HTML con barra de navegación                                |
| `app/templates/index.html`                                        | Página de inicio pública del sitio                                         |
| `app/templates/login.html`                                        | Formulario de login de usuario                                             |
| `app/templates/register.html`                                     | Formulario de registro con selección de rol                                |
| `app/templates/dashboard.html`                                    | Panel principal del usuario autenticado                                    |
| `app/templates/ticket_form.html`                                   | Formulario de creación/edición de cursos                                   |
| `app/templates/tickets.html`                                       | Vista de cursos creados por el usuario                                     |
| `app/templates/usuarios.html`                                     | Listado de usuarios con sus roles (solo para admins)                       |
| `app/templates/cambiar_password.html`                             | Formulario para cambiar la contraseña del usuario                          |
| `static/css/styles.css`                                           | Archivo CSS personalizado (opcional)                                       |
| `database_schema/09_tickets.sql`                                   | SQL para crear la base de datos y tablas del proyecto de tickets            |

---

## 📚 Proyectos Final Asignado

| Nº  | Proyecto                               | CRUD Principal    | Roles                            |
| --- | -------------------------------------- | ----------------- | -------------------------------- |
| 6   | Sistema de Seguimiento de Tickets      | Tickets           | Usuario, Técnico, Admin          |
---

## 🧪 Requisitos previos

- Python 3.8 o superior
- MySQL Server corriendo localmente (`localhost:3306`)
- Un entorno virtual activo (opcional, pero recomendado)

---

## ⚙️ Instalación del proyecto

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/Cruzade-ab/ProyectoFinalComp2052
   cd comp2052/final_project
   ```

2. **Crear entorno virtual y activarlo**

   > Todos los comandos en este paso 2 son opcionales. No requiere correrlos si VSCode no solicita hacerlo. Los comandos en este paso permitirán crear un ambiente virtual para instalar las librería requeridas solamente para este proyecto.

   ```bash
   python -m venv venv   # En Linux/Windows requiere esto
   ```

   ```bash
   python3 -m venv venv     # En Mac requiere esto
   ```

   > Para activar el virtual environment:

   ```bash
   venv\Scripts\activate.bat  # Solo para Windows
   ```

   ```bash
   source venv/bin/activate   # Solo en Linux/Mac requiere esto
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crear la base de datos en MySQL**

   > Para ejecutar el archivo SQL para el proyecto directamente en MySQL:

   ```bash
   mysql -u root -p < database_schema/06_tickets.sql
   ```

   ```bash
   06_tickets.sql
   ```

5. **Ejecutar la aplicación**

   ```bash
   python run.py
   ```

   > Luego abre en tu navegador:

   ```bash
   http://127.0.0.1:5000
   ```

## ✅ Archivos clave

- app/models.py: Modelos SQLAlchemy
- app/forms.py: Formularios personalizados
- app/routes.py: Lógica del CRUD principal
- app/test_routes.py: Lógica del CRUD para pruebas
- templates/\*.html: Vistas HTML para CRUD y autenticación
- database_schema/XX_nombre.sql: Esquema SQL de cada proyecto final
- pruebas/\*.rest: Pruebas para CRUD de las rutas en `test_routes.py`


## 🗂️ Estructura 

```text
📦 raiz_del_proyecto/
├── run.py                 # Punto de entrada de la app Flask
├── config.py              # Configuración global (clave secreta, DB URI)
├── requirements.txt       # Dependencias del proyecto
├── create_demo_users.py   # Script para crear usuarios iniciales (admin, técnico, usuario)
├── README.md              # Documentación del proyecto
├── proyecto.pdf           # Documentación del proyecto requerida para entregar en el curso.
|
├── 📁 pruebas/            # Incluir todos los archivos necesarios para probar el CRUD principal
│   ├── create.rest             # Test file to Create a Row
│   ├── read.rest               # Test file to Read Rows
│   ├── read-a-row.rest         # Test file to Read only one Row
│   ├── update.rest             # Test file to Update a Row
│   ├── delete.rest             # Test file to Delete a Row
|
├── 📁 app/
│   ├── __init__.py             # Inicializa Flask, SQLAlchemy y Blueprints
│   ├── models.py               # Modelos de base de datos (User, Role, Curso)
│   ├── forms.py                # Formularios Flask-WTF (registro, login, curso, contraseña)
│   ├── routes.py               # Rutas protegidas (dashboard, cursos, cambiar contraseña)
│   ├── test_routes.py          # Rutas o end-points para pruebas (cursos)
│   ├── auth_routes.py          # Rutas públicas (login, registro, logout)
|   |
│   ├── 📁 templates/
│   │   ├── layout.html           # Plantilla base para todas las vistas
│   │   ├── index.html            # Página de bienvenida pública
│   │   ├── login.html            # Formulario de inicio de sesión
│   │   ├── register.html         # Formulario de registro con selector de rol
│   │   ├── dashboard.html        # Vista principal del usuario logueado
│   │   ├── ticket_form.html       # Formulario para crear/editar cursos
│   │   ├── tickets.html           # Lista de cursos creados
│   │   ├── usuarios.html         # Vista de administración de usuarios (solo admin)
│   │   └── cambiar_password.html # Formulario para cambiar contraseña
|   |
│   └── 📁 static/
│       └── 📁 css/
│           └── styles.css              # (Opcional) Estilos personalizados
```

## 🧠 Licencia

Este proyecto es de uso académico y puede ser reutilizado con fines educativos indicando las referencias correspondientes del Proyecto. Este proyecto y la lista de proyectos son creaciones originales del profesor Javier A. Dastas de Ciencias de Computadoras.

## 📖 Autores 

Abimael Santa: https://github.com/Cruzade-ab
Génesis Ojeda: https://github.com/DevQueenPR

