# ⚽ FutManager – Plataforma de Gestión de Torneos Deportivos

**FutManager** es una plataforma web en desarrollo que permite organizar, gestionar y promover torneos deportivos comunitarios. Esta es una versión *beta* creada para fines de demostración del proyecto, utilizando Django Rest Framework para el backend (Api-Rest) y Astro para el frontend.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend:** [Astro](https://astro.build/) (Web estática, rutas públicas y privadas)
- **Backend:** [Django](https://www.django-rest-framework.org/) (API REST para consultas y registros simples)
- **Base de Datos:** PostgreSQL (por defecto en Django para desarrollo)
- **Comunicación:** API HTTP (JSON)

---

## 📦 Estructura del Proyecto

```bash
futmanager-project/
│
├── backend/            # Proyecto Django
│   ├── manage.py
│   ├── futmanager/        # Configuración principal
│   └── api/            # App para modelos y vistas (equipos, torneos, etc.)
│
├── frontend/           # Proyecto Astro
│   ├── public/
│   ├── src/
│   └── astro.config.mjs
│
├── README.md
└── .gitignore
