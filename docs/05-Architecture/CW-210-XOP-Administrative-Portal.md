---
id: CW-210
code: CW-210
title: XOP Administrative Portal Architecture
version: 1.0.0
status: APPROVED
owner: Enterprise Architecture
authors:
  - CelebraWeb Platform
approvers:
  - Enterprise Architect
  - Product Owner
created: 2026-07-08
updated: 2026-07-08
tags:
  - architecture
  - portal
  - xop
  - frontend
---

# CW-210 — XOP Administrative Portal Architecture

---

# 1. Propósito

El XOP Administrative Portal es la arquitectura funcional oficial para todos los productos desarrollados sobre la XOP Platform.

Su propósito es proporcionar una experiencia de administración consistente, escalable y reutilizable para todos los productos de la plataforma, independientemente de su dominio de negocio.

El Portal Administrativo constituye el punto único de entrada para los usuarios autenticados y representa la capa de interacción entre las capacidades empresariales de la plataforma y los usuarios finales.

Este documento establece la arquitectura oficial que deberá respetarse durante la evolución de la plataforma.

---

# 2. Alcance

Esta arquitectura aplica para todos los productos construidos sobre XOP Platform.

Entre ellos, sin limitarse a:

- CelebraWeb
- Analytics Solutions Q
- Wedding Platform
- Club Management
- Productos futuros desarrollados sobre XOP Platform

Todos los productos compartirán el mismo Portal Administrativo y utilizarán esta arquitectura como referencia obligatoria.

---

# 3. Objetivos Arquitectónicos

La arquitectura del Portal Administrativo persigue los siguientes objetivos:

- Proporcionar una experiencia uniforme para todos los productos.
- Centralizar la navegación de la plataforma.
- Reducir duplicidad de interfaces.
- Facilitar la incorporación de nuevos módulos.
- Mantener independencia entre el Portal y la lógica de negocio.
- Permitir la evolución continua sin rediseños estructurales.
- Favorecer la reutilización de componentes.
- Facilitar la incorporación de nuevos productos sobre XOP Platform.

---

# 4. Principio Fundamental

El Portal Administrativo pertenece a la plataforma XOP.

No pertenece a un producto específico.

Los productos se integran al Portal.

El Portal nunca se rediseña para adaptarse a un producto.

Los productos deben adaptarse a la arquitectura oficial del Portal.

---

# Estado

**Documento en construcción.**

---

# 5. Principios Arquitectónicos

La arquitectura del XOP Administrative Portal se rige por los siguientes principios obligatorios.

## 5.1 Single Entry Point

Todo usuario autenticado accede a la plataforma mediante un único Portal Administrativo.

No existen múltiples portales para un mismo producto.

Todos los módulos se integran al Portal.

---

## 5.2 Platform First

El Portal pertenece a la XOP Platform.

Nunca pertenece a un producto específico.

Los productos utilizan el Portal.

El Portal nunca se adapta a un producto.

---

## 5.3 Business Capability First

El Portal organiza capacidades empresariales.

No organiza pantallas.

Cada opción del menú representa una capacidad del negocio.

Nunca una implementación técnica.

---

## 5.4 Composition over Duplication

Todo nuevo módulo se incorpora reutilizando componentes existentes.

La duplicación de layouts, navegación o componentes está prohibida.

---

## 5.5 Responsive by Design

Toda funcionalidad del Portal deberá ser completamente responsive.

La experiencia deberá mantenerse consistente en escritorio, tablet y dispositivos móviles.

---

## 5.6 Security by Default

Toda navegación se considera protegida.

Ningún módulo podrá asumir autenticación implícita.

Toda autorización deberá realizarse mediante los mecanismos oficiales de autenticación y control de acceso de la plataforma.

---

## 5.7 Tenant Awareness

Toda capacidad integrada al Portal deberá operar considerando el Tenant activo.

Ningún componente podrá asumir contexto global sin considerar la organización seleccionada.

---

## 5.8 Consistent User Experience

Todos los productos construidos sobre XOP Platform compartirán una experiencia uniforme.

La navegación, estructura, componentes visuales y comportamiento deberán mantenerse consistentes independientemente del producto utilizado.

---

## 5.9 Extensibility

La incorporación de nuevos módulos deberá realizarse mediante integración.

Nunca mediante rediseños estructurales del Portal.

---

## 5.10 Evolution without Redesign

La evolución del Portal deberá realizarse mediante crecimiento incremental.

Los cambios arquitectónicos sólo podrán realizarse cuando exista una necesidad demostrada y documentada mediante una Architectural Decision Record (ADR) o el Decision Log oficial del proyecto.

---

Estos principios son obligatorios para cualquier equipo o producto que utilice el XOP Administrative Portal.

---

# 6. Modelo Conceptual del Portal

El XOP Administrative Portal constituye la capa funcional que conecta a los usuarios autenticados con las capacidades empresariales de la plataforma.

El Portal no implementa lógica de negocio.

Su responsabilidad consiste en organizar, presentar y orquestar el acceso a las capacidades disponibles dentro de XOP Platform.

Conceptualmente, el Portal se compone de los siguientes dominios funcionales.

```
                     XOP PLATFORM
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
 Authentication                    Platform Services
 Authorization                     Configuration
 Audit                             Notifications
 Metrics                           Scheduler
 AI Services                       Integrations
        │
        ▼
┌─────────────────────────────────────────────────────┐
│              XOP Administrative Portal              │
├─────────────────────────────────────────────────────┤
│ Header                                              │
│ Sidebar                                             │
│ Workspace                                           │
│ Footer                                              │
│ Notification Center                                 │
│ User Profile                                        │
│ Search                                               │
│ Breadcrumb                                          │
│ Quick Actions                                       │
│ Widget Container                                    │
└─────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────┐
│               Business Capabilities                 │
├─────────────────────────────────────────────────────┤
│ Dashboard                                           │
│ Organizations                                       │
│ Users                                               │
│ Roles                                               │
│ Events                                              │
│ Invitations                                         │
│ Finance                                             │
│ Analytics                                           │
│ Configuration                                       │
│ Platform Administration                             │
│ Artificial Intelligence                             │
└─────────────────────────────────────────────────────┘
```

El Portal constituye una capa de orquestación.

No pertenece a ninguna capacidad empresarial.

Cada módulo representa una Business Capability independiente que se integra al Portal mediante contratos bien definidos.

La incorporación de nuevas capacidades no modifica la arquitectura del Portal.

Únicamente amplía las capacidades disponibles para el usuario.

Esta separación garantiza que la evolución funcional del producto no implique rediseños estructurales del Frontend.

---

## Responsabilidades del Portal

El Portal es responsable de:

- Administrar la navegación global.
- Mostrar el contexto del usuario autenticado.
- Mostrar el Tenant activo.
- Orquestar el acceso a las capacidades empresariales.
- Centralizar la experiencia de usuario.
- Administrar componentes compartidos.
- Administrar el estado global de la plataforma.
- Integrar servicios transversales.
- Garantizar consistencia visual.
- Proporcionar extensibilidad para nuevos módulos.

---

## Responsabilidades que NO pertenecen al Portal

El Portal nunca deberá:

- Implementar reglas de negocio.
- Ejecutar procesos empresariales.
- Contener lógica específica de un producto.
- Duplicar componentes funcionales.
- Administrar persistencia.
- Implementar autorización específica de un módulo.
- Acoplarse a una Business Capability particular.

Estas responsabilidades pertenecen exclusivamente a los módulos funcionales correspondientes.
---

# 7. Componentes Oficiales del Portal

El XOP Administrative Portal está compuesto por un conjunto limitado de componentes estructurales.

Estos componentes constituyen la arquitectura visual oficial de la plataforma.

Ningún producto podrá modificar esta estructura.

Los nuevos módulos deberán integrarse utilizando exclusivamente estos componentes.

---

## 7.1 Header

El Header constituye la barra superior permanente del Portal.

Responsabilidades:

- Identidad de la plataforma.
- Producto activo.
- Organización (Tenant) activa.
- Buscador global.
- Centro de notificaciones.
- Acciones rápidas.
- Perfil del usuario.
- Configuración personal.
- Cierre de sesión.

El Header nunca contendrá navegación funcional.

---

## 7.2 Sidebar

El Sidebar constituye el mecanismo oficial de navegación.

Cada opción representa una Business Capability.

Nunca una implementación técnica.

Ejemplos:

- Dashboard
- Organizations
- Users
- Roles
- Events
- Finance
- Analytics
- Configuration
- Platform Administration

La estructura del Sidebar deberá permanecer consistente para todos los productos.

---

## 7.3 Workspace

El Workspace representa el área principal de trabajo.

Toda Business Capability se renderiza dentro del Workspace.

El Portal nunca reemplaza el Workspace.

Únicamente cambia el módulo activo.

---

## 7.4 Footer

El Footer representa la información institucional de la plataforma.

Podrá contener:

- versión del producto;
- versión de la plataforma;
- enlaces institucionales;
- estado de servicios;
- información legal.

No contendrá lógica de negocio.

---

## 7.5 Notification Center

Componente responsable de centralizar todas las notificaciones del Portal.

Integrará capacidades como:

- alertas;
- tareas;
- eventos;
- mensajes;
- auditoría;
- monitoreo.

---

## 7.6 User Profile

Área responsable de representar el contexto del usuario autenticado.

Mostrará:

- nombre;
- fotografía;
- organización activa;
- roles;
- preferencias;
- cierre de sesión.

---

## 7.7 Global Search

Servicio transversal que permitirá localizar capacidades, registros y acciones disponibles dentro de la plataforma.

Su implementación será progresiva.

---

## 7.8 Breadcrumb

Representa la ubicación actual del usuario dentro del Portal.

Su objetivo consiste en mejorar la orientación durante la navegación.

---

## 7.9 Quick Actions

Área destinada a exponer las acciones más utilizadas por el usuario.

Estas acciones serán configurables según:

- permisos;
- producto;
- tenant;
- contexto.

---

## 7.10 Widget Container

El Dashboard utilizará Widgets independientes.

Cada Widget constituye una unidad reutilizable.

Ejemplos:

- KPIs
- Calendario
- Actividad reciente
- Alertas
- Pendientes
- Indicadores
- IA
- Reportes

Los Widgets nunca dependerán entre sí.

Su incorporación o eliminación no modificará la arquitectura del Portal.

---

# Regla Arquitectónica

Toda nueva capacidad visual deberá integrarse reutilizando los componentes definidos en este capítulo.

La creación de nuevos componentes estructurales requerirá aprobación del Enterprise Architect y deberá registrarse en el Decision Log oficial.
