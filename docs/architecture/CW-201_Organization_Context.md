---
id: CW-201
code: CW-201
title: Organization Context
version: 1.0.0
status: APPROVED
owner: Platform Team
type: Business Capability
sprint: 10
---

# 1. Objetivo

Definir el mecanismo oficial mediante el cual cada petición conocerá el contexto organizacional del usuario autenticado.

El Organization Context será utilizado por todos los módulos de la plataforma para garantizar el aislamiento de información entre organizaciones (Multi-Tenant).

---

# 2. Alcance

Aplica a:

- API REST
- Services
- Repositories
- Business Rules
- Auditoría
- Logging
- Analytics
- IA

---

# 3. Flujo

```text
HTTP Request
      │
      ▼
Bearer Token
      │
      ▼
JWTService
      │
      ▼
get_current_user()
      │
      ▼
Organization Context
      │
      ▼
Business Service
      │
      ▼
Repository
      │
      ▼
Database
```

---

# 4. Información disponible

El contexto deberá contener como mínimo:

- User Id
- Organization Id
- Email
- Nombre
- Apellidos
- Super Admin
- Estado

En futuras versiones se agregarán:

- Roles
- Permissions
- Language
- Timezone
- Culture
- Correlation Id

---

# 5. Reglas

1. Ningún Repository deberá consultar información de otra organización.

2. Ningún Service recibirá directamente entidades ORM como contexto de autenticación.

3. Todo acceso a datos deberá realizarse utilizando el Organization Context.

4. El contexto será creado únicamente por el Platform Core.

---

# 6. Beneficios

- Aislamiento Multi-Tenant.
- Desacoplamiento entre autenticación y negocio.
- Base para RBAC.
- Base para Auditoría.
- Base para IA.
- Escalabilidad.

---

# 7. Estado

APPROVED