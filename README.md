#  Nexus — Sistema de Información para Hogares Geriátricos

Nexus es una aplicación web pensada para la gestión integral de un hogar
geriátrico: residentes, personal de cuidado, agenda de actividades y
medicamentos, seguimiento familiar, historial clínico/asistencial y
notificaciones de alertas. Todo desde un solo panel, con roles de acceso
diferenciados (Administrador, Cuidador, Familiar).

Construido con **FastAPI** + **MariaDB/MySQL** + **Jinja2** + **Bootstrap 5**.

---

## Equipo Nexus

- Dilan Carreño
- Jarek Luque
- Joshua Nocua
- Susan López

Proyecto desarrollado como parte del programa **Tecnólogo en Análisis y
Desarrollo de Software** — SENA.

---

##  Funcionalidades

| Módulo | Descripción |
|---|---|
|  **Autenticación** | Login, registro y roles (Administrador, Cuidador, Familiar) |
|  **Residentes** | Registro completo: datos personales, diagnóstico, alergias, familiar responsable |
|  **Personal** | Gestión de cuidadores, turnos, estado activo/inactivo y panel individual con sus actividades asignadas |
|  **Asignaciones** | El administrador asigna residentes a cada cuidador; el cuidador solo ve (y su historial solo muestra) lo suyo |
|  **Agenda** | Calendario de actividades y medicamentos por residente, con horas, días y cuidador asignado |
|  **Medicamentos** | Control de medicamentos por residente: dosis, horario y observaciones |
|  **Vista Familiar** | Panel de solo lectura para que un familiar consulte el estado de su residente |
|  **Historial** | Bitácora de actividades y medicamentos aplicados, registrada automáticamente desde la agenda |
|  **Notificaciones** | Alertas generadas automáticamente a la hora programada, con estado Pendiente / Completada — completar y eliminar |
|  **Reporte PDF** | Reporte del cuidador con sus residentes, actividades y medicamentos |
|  **API** | API REST en JSON documentada en `/docs` |
|  **Usuarios** | Panel exclusivo de Administrador para gestionar las cuentas del sistema |

---

##  Tecnologías

- **FastAPI** — backend y enrutamiento
- **Jinja2** — plantillas del lado del servidor
- **MariaDB / MySQL** (PyMySQL) — base de datos
- **Bootstrap 5.3** — estilos base
- **Starlette SessionMiddleware** — sesiones de usuario
- **Node.js** — generación de reportes PDF (`generar_pdf.js`)

---

##  Instalación y ejecución

Requisitos: Python 3.10+, MariaDB 10.4+ / MySQL 8 (por ejemplo XAMPP) y Node.js (solo para `generar_pdf.js`).

### 1. Crear y activar el entorno virtual

**Windows**
```bash
cd Nexus
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac**
```bash
cd Nexus
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
npm install
```


### 3. Usuarios de prueba

| Rol | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin` | `admin123` |
| Cuidador | `cuidador` | `cuidador123` |
| Familiar | `familiar` | `familiar123` |


### 4. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

- Aplicación: `http://localhost:8000/` (redirige al login o al panel según la sesión).
- Documentación Swagger: `http://localhost:8000/docs` (única ruta de la documentación). La API REST está bajo `/api/v1`.

---

##Estructura del proyecto

```
Nexus/
├── main.py                     # Creación de la app, middleware, lifespan, include_router
├── generar_pdf.js              # Generación del reporte PDF
├── requirements.txt
├── core/
│   ├── config.py                # Rutas base, SECRET_KEY, SMTP, roles, constantes
│   ├── security.py               # Hash de contraseñas
│   ├── templates.py              # Jinja2Templates, render(), flash()
│   ├── auth.py                    # login_required / admin_required / staff_required
│   ├── acceso.py                  # Residentes visibles según el rol
│   ├── agenda.py / itinerario.py  # Agenda de actividades y medicamentos
│   ├── fechas.py                  # Texto legible de los días programados
│   ├── residentes.py / email.py
│   └── tasks.py                   # Tarea en segundo plano de notificaciones (RF05)
├── database/
│   ├── connection.py             # get_db()
│   ├── schema.py                  # init_db(): ejecuta nexus_v3.sql
│   └── nexus_v3.sql               # Esquema + datos iniciales (MariaDB/MySQL)
├── routers/
│   ├── auth.py                    # /, /login, /registro, /logout
│   ├── api.py                     # API REST /api/v1
│   ├── dashboard.py
│   ├── residentes.py
│   ├── agenda.py
│   ├── itinerario.py
│   ├── asignaciones.py
│   ├── pdf.py
│   ├── horarios.py
│   ├── usuarios.py
│   ├── familiar.py
│   ├── medicamentos.py
│   ├── personal.py
│   ├── historial.py
│   ├── notificaciones.py
│   └── perfil.py
├── static/
│   ├── css/nexus.css
│   └── img/logo.png
└── templates/
    ├── base.html
    ├── login.html / registro.html
    ├── dashboard.html
    ├── residentes/
    ├── personal/
    ├── agenda/
    ├── asignaciones/
    ├── horarios/
    ├── medicamentos/
    ├── familiar/
    ├── historial/
    ├── notificaciones/
    ├── perfil/
    └── usuarios/
```


---

## Roles del sistema

- **Administrador** — acceso total, incluida la gestión de usuarios.
- **Cuidador** — acceso operativo: residentes, agenda, medicamentos, personal, historial y notificaciones.
- **Familiar** — acceso restringido únicamente a `/familiar` en modo lectura. El resto de los módulos
  responde con un redireccionamiento y un mensaje de permisos (`staff_required` en `main.py`).

---


Equipo Nexus. 💙