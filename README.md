# 🏠 Portal Inmobiliario

Plataforma desarrollada en **Django** para conectar **arrendadores** y **arrendatarios**, simplificando la búsqueda y publicación de propiedades en arriendo.  

---

## 🚀 Funcionalidades principales

### 🔐 Autenticación y perfiles
- Registro y login de usuarios.
- Modelo de usuario extendido (`PerfilUser`) con:
  - Tipo de usuario (Arrendador / Arrendatario).
  - RUT.
  - Imagen de perfil.
- Cada usuario puede editar solo su propio perfil (UpdateView con restricción).

### 📄 Secciones del portal
- **Home (`index.html`)**  
  - Imagen destacada (`media/inmuebles/1casapiloto.png`).  
  - Título llamativo, subtítulo y botón de acción “Contáctanos”.  
- **Acerca (`acerca.html`)**  
  - Información sobre el proyecto.  
  - Invitación a propietarios y arrendatarios.  
  - Presentación del equipo profesional.  
- **Contacto (`contacto.html`)**  
  - Formulario para guardar consultas en la base de datos.  
  - Campos: Nombre, Correo, Mensaje.  
  - Mensaje de confirmación al enviar.  

### 🖼️ Gestión de imágenes
- Configuración de `MEDIA_URL` y `MEDIA_ROOT`.  
- Estructura de carpetas:  
  - `media/fotos_perfil/` → imágenes de usuarios.  
  - `media/inmuebles/` → imágenes de propiedades.  

### 🖌️ Layouts compartidos
- **`navbar.html`**: Menú con enlaces a Home, Servicios, Acerca, Contacto y Perfil.  
- **`footer.html`**: Pie de página con información y links útiles.  
- **`scripts.html`** y **`scripts_footer.html`**: Archivos centralizados para carga de scripts.  

---

## 📂 Estructura del proyecto
```bash
backend/
 ├── media/
 │   ├── fotos_perfil/
 │   └── inmuebles/
 │       ├── 1casapiloto.png
 │       ├── casa2.jpeg
 │       └── sin_imagen.png
 └── portal/
     └── templates/
         ├── web/componentes/
         │   ├── navbar.html
         │   ├── footer.html
         │   ├── scripts.html
         │   └── scripts_footer.html
         ├── web/
         │   ├── index.html
         │   ├── acerca.html
         │   └── contacto.html
         └── usuarios/
             └── perfil_form.html
```

🛠️ Tecnologías utilizadas

Django 4.x
Python 3.9+
Bootstrap 5 (estilos y componentes)
SQLite3 (desarrollo, fácil despliegue)

▶️ Cómo ejecutar el proyecto con Docker Compose

### Clonar repositorio
git clone <repo_url>
cd portal_inmobiliario

### Construir y levantar contenedores
docker-compose up --build

### Aplicar migraciones
docker-compose exec web python manage.py migrate

### Crear superusuario
docker-compose exec web python manage.py createsuperuser

### Acceder al proyecto
Aplicación: 👉 http://localhost:8000
Admin Django: 👉 http://localhost:8000/admin

🚀 Próximos pasos

📌 Publicación de inmuebles con filtros avanzados.

📊 Panel de administración para arrendadores.

📱 Mejoras en la experiencia móvil (UI/UX).