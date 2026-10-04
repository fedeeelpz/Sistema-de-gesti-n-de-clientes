# Sistema de Gestión Backoffice

Sistema web simple para gestionar clientes y sus deudas (fiados), desarrollado con Django. Pensado para reemplazar el registro manual en papel de un comercio.

## Funcionalidades

- Listado de clientes con nombre, monto adeudado, fecha y estado
- Alta de nuevos clientes
- Edición de clientes existentes (nombre, monto, estado)
- Eliminación de clientes
- Búsqueda de clientes por nombre
- Estados de deuda: **Pendiente** o **Pagado**
- Panel de administración de Django para gestión avanzada

## Tecnologías

- Python
- Django
- SQLite (base de datos local)
- HTML / CSS

## Instalación

1. Cloná el repositorio

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd https://github.com/fedeeelpz/Sistema-de-gesti-n-de-clientes
```

2. Creá y activá un entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

3. Instalá las dependencias

```bash
pip install -r requirements.txt
```

4. Aplicá las migraciones

```bash
cd sistema_clientes
python manage.py migrate
```

5. Creá un superusuario (para acceder al panel de administración)

```bash
python manage.py createsuperuser
```

6. Corré el servidor

```bash
python manage.py runserver
```

7. Accedé a la aplicación

- Sitio principal: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## Estructura del proyecto
sistema_clientes/
├── manage.py
├── sistema_clientes/       # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── clientes/               # App principal
    ├── models.py           # Modelo Cliente
    ├── views.py            # Lógica de listado, alta, edición y borrado
    ├── forms.py            # Formulario de alta de clientes
    ├── urls.py             # Rutas de la app
    ├── admin.py            # Configuración del panel admin
    ├── templates/clientes/ # Templates HTML
    └── static/clientes/    # Archivos CSS

## Estado del proyecto

En desarrollo. Corre actualmente solo en entorno local.