---
id: CW-500
code: CW-500
title: Engineering Handbook
version: 1.0.0
status: DRAFT
classification: INTERNAL

owner: Enterprise Architecture

created: 2026-06-30
updated: 2026-06-30

repository: docs/06-Engineering/CW-500-Engineering-Handbook.md

references:
  - CW-000
  - CW-001
  - CW-002
---

# CW-500 Engineering Handbook

# Control del Documento

| Campo | Valor |
|--------|-------|
| Código | CW-500 |
| Nombre | Engineering Handbook |
| Estado | DRAFT |
| Versión | 1.0.0 |

---

# 1. Propósito

El Engineering Handbook constituye la documentación técnica oficial de CelebraWeb.

Describe la implementación real del software, su arquitectura, componentes, convenciones y evolución técnica.

Este documento se actualiza conforme evoluciona el código fuente y representa el estado actual de la plataforma.

---

# 2. Alcance

Este documento cubre:

- Arquitectura técnica.
- Organización del repositorio.
- Backend.
- Frontend.
- Base de datos.
- APIs.
- Patrones de diseño.
- Convenciones de desarrollo.
- Historial de implementación por Sprint.

No reemplaza la documentación estratégica ni funcional definida en la Foundation.

---

# 3. Arquitectura General

La implementación actual de CelebraWeb sigue una arquitectura por capas (Layered Architecture), cuyo objetivo es separar las responsabilidades del sistema y facilitar su mantenimiento, evolución y escalabilidad.

La comunicación entre las capas se realiza de manera descendente, evitando dependencias innecesarias.

```text
Cliente

↓

API (Endpoints)

↓

Services (Lógica de negocio)

↓

Repositories (Acceso a datos)

↓

Database

↓

PostgreSQL
```

## Principios aplicados

- Separación de responsabilidades.
- Alta cohesión.
- Bajo acoplamiento.
- Reutilización de componentes.
- Escalabilidad.
- Mantenibilidad.

---

# 4. Organización del Repositorio

La estructura principal del proyecto es la siguiente:

```text
CelebraWeb/

backend/
frontend/
docs/
```

## backend

Contiene toda la lógica de negocio y la implementación del servidor.

## frontend

Reservado para la interfaz de usuario de la plataforma.

Actualmente no contiene implementación.

## docs

Contiene la documentación corporativa y técnica del proyecto.

Toda la documentación oficial debe mantenerse sincronizada con el código fuente.

---

# 5. Arquitectura del Backend

El backend se desarrolla utilizando FastAPI y adopta una arquitectura modular organizada por responsabilidades.

La estructura implementada actualmente es la siguiente:

```text
backend/

app/

api/
core/
database/
models/
repositories/
schemas/
services/

main.py
```

Cada carpeta cumple una responsabilidad específica dentro de la arquitectura.

---

## api

Contiene los endpoints REST expuestos por la plataforma.

Su responsabilidad es recibir las solicitudes HTTP, validar la entrada y delegar la ejecución a la capa de servicios.

No debe contener lógica de negocio.

---

## services

Implementa la lógica de negocio de la aplicación.

Los servicios coordinan las operaciones necesarias para ejecutar cada caso de uso utilizando repositorios y otros componentes.

Toda regla de negocio debe implementarse en esta capa.

---

## repositories

Implementa el acceso a la base de datos.

Los repositorios encapsulan las operaciones de persistencia y aíslan la lógica de acceso a datos del resto de la aplicación.

---

## database

Contiene la configuración de la base de datos y los componentes compartidos relacionados con la persistencia.

---

## models

Contendrá las entidades persistentes del sistema.

Actualmente la estructura se encuentra preparada para su crecimiento.

---

## schemas

Contendrá los modelos de intercambio utilizados por FastAPI para validar solicitudes y respuestas.

---

## core

Reservado para componentes transversales del sistema.

Entre ellos:

- configuración
- seguridad
- autenticación
- utilidades comunes
- constantes globales

---

# 6. Flujo General de una Solicitud

Todas las solicitudes siguen el siguiente flujo:

```text
Cliente

↓

API

↓

Service

↓

Repository

↓

Database

↓

PostgreSQL

↓

Repository

↓

Service

↓

API

↓

Cliente
```

Cada capa tiene una única responsabilidad, facilitando las pruebas, el mantenimiento y la evolución del software.
---

# 7. Tecnologías Base

La implementación actual de CelebraWeb utiliza una arquitectura basada en tecnologías modernas orientadas al desarrollo de aplicaciones empresariales.

| Componente | Tecnología | Estado |
|------------|------------|--------|
| Backend | FastAPI | Implementado |
| Lenguaje | Python | Implementado |
| Base de Datos | PostgreSQL | Implementado |
| Contenedores | Docker | Implementado |
| Control de Versiones | Git | Implementado |

La incorporación de nuevas tecnologías deberá ser aprobada mediante revisión de arquitectura y responder a una necesidad técnica o funcional claramente identificada.

---

# 8. Principios de Desarrollo

Todo desarrollo dentro de CelebraWeb deberá cumplir los siguientes principios:

## Separación de responsabilidades

Cada componente deberá tener una única responsabilidad claramente definida.

---

## Reutilización

Las funcionalidades comunes deberán implementarse una sola vez y reutilizarse siempre que sea posible.

---

## Simplicidad

La solución más simple que resuelva correctamente el problema será la opción preferida.

---

## Escalabilidad

Toda implementación deberá permitir la incorporación de nuevas funcionalidades sin requerir modificaciones estructurales significativas.

---

## Mantenibilidad

El código deberá ser claro, legible y fácil de mantener por cualquier integrante del equipo.

---

## Consistencia

Las nuevas implementaciones deberán respetar la arquitectura, las convenciones y los estándares definidos para el proyecto.

---

# 9. Convenciones Generales

## Organización

Cada módulo deberá mantener la estructura establecida por la arquitectura del proyecto.

## Nombres

Los nombres de archivos, clases, funciones y variables deberán ser descriptivos y consistentes.

## Comentarios

Los comentarios deberán explicar el propósito de una decisión cuando ésta no sea evidente en el código.

No deberán utilizarse comentarios para describir instrucciones obvias.

## Versionamiento

Todo cambio deberá registrarse mediante Git y asociarse al Sprint correspondiente.

---

# 10. Estado Actual de Implementación

A la fecha de esta versión del documento, la plataforma presenta el siguiente nivel de implementación.

| Componente | Estado |
|------------|--------|
| Arquitectura Base | Implementado |
| FastAPI | Implementado |
| Organización del Proyecto | Implementado |
| Base de Datos | Implementado |
| Repository Pattern | Implementado |
| Service Layer | Implementado |
| API REST Base | Implementado |
| Frontend | Pendiente |
| Autenticación | Pendiente |
| Experiences | Pendiente |
| RSVP | Pendiente |
| Check-In | Pendiente |

Este estado deberá actualizarse al finalizar cada Sprint de desarrollo.

---

# 11. Backend

El backend de CelebraWeb está desarrollado utilizando FastAPI y constituye el núcleo de la plataforma.

Actualmente implementa la configuración inicial de la aplicación, el registro de rutas y el punto de entrada principal del servidor.

La arquitectura sigue una organización modular basada en responsabilidades.

---

## 11.1 Archivo `main.py`

**Ubicación**

```text
backend/app/main.py
```

### Propósito

`main.py` es el punto de entrada principal de la aplicación.

Su responsabilidad es inicializar FastAPI, registrar los módulos disponibles y exponer el estado general de la API.

No contiene lógica de negocio.

---

### Responsabilidades

El archivo realiza las siguientes funciones:

- Crear la instancia principal de FastAPI.
- Definir la información básica de la API.
- Registrar los routers disponibles.
- Exponer un endpoint raíz para validar el funcionamiento del servicio.

---

### Inicialización de FastAPI

La aplicación se inicializa mediante una única instancia de FastAPI.

Actualmente la configuración incluye:

| Parámetro | Valor |
|-----------|-------|
| Title | CelebraWeb API |
| Version | 0.1.0 |

Esta información se utiliza para identificar la API y alimentar automáticamente la documentación generada por FastAPI.

---

### Registro de Routers

Actualmente la aplicación registra el módulo:

```text
organizations_router
```

Todas las rutas de este módulo se publican bajo el prefijo:

```text
/api/v1
```

Esta estructura permite versionar la API y facilita la incorporación de nuevos módulos sin afectar la organización general del proyecto.

---

### Endpoint de Estado

La aplicación implementa un endpoint raíz:

```text
GET /
```

Su objetivo es verificar que el servicio se encuentra disponible.

La respuesta actual contiene:

| Campo | Descripción |
|--------|-------------|
| product | Nombre del producto |
| version | Versión de la API |
| status | Estado del servicio |

Este endpoint actúa como una validación básica de disponibilidad (health check funcional).

---

### Flujo de Inicialización

```text
Inicio del servidor

↓

Crear instancia FastAPI

↓

Registrar routers

↓

Aplicación lista para recibir solicitudes
```

---

### Dependencias

El archivo depende de:

- FastAPI.
- Router del módulo Organizations.

No presenta dependencias directas con la base de datos ni contiene lógica de negocio.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 1 y Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- Existe un único punto de entrada para toda la aplicación.
- La API utiliza versionamiento mediante el prefijo `/api/v1`.
- La organización modular permite incorporar nuevos routers sin modificar la arquitectura existente.
- La lógica de negocio permanece fuera del archivo `main.py`, respetando el principio de separación de responsabilidades.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Inicialización FastAPI | Implementado |
| Registro de routers | Implementado |
| Endpoint raíz | Implementado |
| Versionamiento de API | Implementado |
---

## 11.2 Archivo `database.py`

**Ubicación**

```text
backend/app/database/database.py
```

### Propósito

El archivo `database.py` centraliza la configuración de acceso a la base de datos utilizada por CelebraWeb.

Su responsabilidad es crear la conexión principal (Engine) y configurar el mecanismo mediante el cual la aplicación obtiene sesiones de trabajo con la base de datos.

No contiene lógica de negocio ni consultas SQL.

---

### Responsabilidades

Este archivo implementa las siguientes funciones:

- Cargar las variables de entorno.
- Obtener la cadena de conexión de la base de datos.
- Crear el Engine de SQLAlchemy.
- Configurar el administrador de sesiones (`SessionLocal`).

---

### Carga de Configuración

La configuración de conexión se obtiene desde variables de entorno utilizando la biblioteca **python-dotenv**.

La variable utilizada actualmente es:

| Variable | Descripción |
|----------|-------------|
| DATABASE_URL | Cadena de conexión a PostgreSQL |

Esta aproximación evita almacenar información sensible directamente dentro del código fuente.

---

### Engine de SQLAlchemy

La conexión principal se crea mediante `create_engine()`.

Actualmente se encuentra configurada con:

| Parámetro | Valor |
|-----------|-------|
| echo | True |

La opción `echo=True` permite visualizar las sentencias SQL generadas por SQLAlchemy durante la ejecución de la aplicación.

Esta configuración facilita las actividades de desarrollo y depuración.

---

### Administrador de Sesiones

El archivo define un único objeto `SessionLocal`, responsable de crear las sesiones utilizadas por los repositorios para interactuar con la base de datos.

La configuración actual es:

| Parámetro | Valor |
|-----------|-------|
| autocommit | False |
| autoflush | False |

Esta configuración proporciona control explícito sobre las transacciones y el envío de cambios hacia la base de datos.

---

### Flujo de Inicialización

```text
Inicio de la aplicación

↓

Carga variables de entorno

↓

Obtiene DATABASE_URL

↓

Crea Engine

↓

Configura SessionLocal

↓

Disponible para los repositorios
```

---

### Dependencias

El archivo depende de:

- SQLAlchemy.
- python-dotenv.
- Variables de entorno del sistema.

No presenta dependencias con los módulos funcionales de CelebraWeb.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 1 y Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- Existe un único punto central para la configuración de la base de datos.
- La configuración utiliza variables de entorno para desacoplar el código del entorno de ejecución.
- La administración de sesiones queda separada de la lógica de negocio y de los repositorios.
- La arquitectura facilita la reutilización del mismo mecanismo de conexión en toda la plataforma.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Variables de entorno | Implementado |
| Engine SQLAlchemy | Implementado |
| SessionLocal | Implementado |
| Configuración PostgreSQL | Implementado |
---

## 11.3 Archivo `base.py`

**Ubicación**

```text
backend/app/database/base.py
```

### Propósito

El archivo `base.py` define la clase base utilizada por SQLAlchemy para la creación de todas las entidades persistentes de CelebraWeb.

Esta clase constituye el punto de partida sobre el cual se construirán todos los modelos del sistema.

No contiene lógica de negocio ni configuración de la base de datos.

---

### Responsabilidades

Actualmente este archivo tiene una única responsabilidad:

- Definir la clase base (`Base`) que heredarán todas las entidades del modelo de datos.

---

### Implementación

La clase `Base` hereda de `DeclarativeBase`, proporcionado por SQLAlchemy.

Esta implementación permite utilizar el modelo declarativo para definir las tablas de la base de datos mediante clases de Python.

Toda entidad persistente deberá heredar de esta clase.

---

### Flujo de utilización

```text
DeclarativeBase

↓

Base

↓

Entidad (Organization)

↓

Entidad (User)

↓

Entidad (Experience)

↓

...
```

La clase `Base` actúa como el ancestro común de todas las entidades del dominio.

---

### Dependencias

El archivo depende únicamente de:

- SQLAlchemy ORM.

No presenta dependencias con otros módulos de la plataforma.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 1 y Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- Existe una única clase base para todas las entidades.
- Se adopta el modelo declarativo de SQLAlchemy.
- La definición de entidades queda desacoplada de la configuración de conexión.
- La arquitectura facilita la incorporación de nuevos modelos manteniendo consistencia en toda la plataforma.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Clase Base | Implementado |
| Modelo Declarativo | Implementado |
| Preparado para entidades | Implementado |
---

## 11.4 Archivo `organizations.py`

**Ubicación**

```text
backend/app/api/v1/organizations.py
```

### Propósito

El archivo `organizations.py` implementa el primer controlador (Router) de la API REST de CelebraWeb.

Su responsabilidad es exponer los endpoints relacionados con la administración de organizaciones y delegar la ejecución de la lógica de negocio a la capa de servicios.

No contiene reglas de negocio ni acceso directo a la base de datos.

---

### Responsabilidades

Actualmente el controlador implementa las siguientes funciones:

- Registrar el módulo Organizations dentro de la API.
- Definir el prefijo de las rutas.
- Asociar el módulo a la documentación automática de FastAPI.
- Delegar las solicitudes al servicio correspondiente.

---

### Configuración del Router

El módulo utiliza un `APIRouter` con la siguiente configuración.

| Parámetro | Valor |
|-----------|-------|
| Prefix | `/organizations` |
| Tags | `Organizations` |

El prefijo agrupa todas las rutas relacionadas con organizaciones bajo un mismo recurso REST.

La etiqueta (`tag`) permite organizar automáticamente la documentación OpenAPI generada por FastAPI.

---

### Servicio Asociado

El controlador crea una instancia de:

```text
OrganizationService
```

Toda la lógica de negocio se ejecuta en dicho servicio.

El controlador únicamente recibe la solicitud HTTP y retorna el resultado.

---

### Endpoint Implementado

Actualmente existe un único endpoint.

| Método | Ruta | Descripción |
|---------|------|-------------|
| GET | `/organizations/` | Obtiene el listado de organizaciones |

Este endpoint es publicado finalmente como:

```text
GET /api/v1/organizations/
```

gracias al prefijo definido en `main.py`.

---

### Flujo de Ejecución

```text
Cliente

↓

GET /api/v1/organizations/

↓

organizations.py

↓

OrganizationService

↓

Repository

↓

Database

↓

Respuesta
```

El controlador no interactúa directamente con la base de datos.

Toda la comunicación ocurre a través de la capa de servicios.

---

### Dependencias

El archivo depende de:

- FastAPI.
- OrganizationService.

No depende directamente de SQLAlchemy ni de los repositorios.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- Uso de APIRouter para desacoplar módulos de la aplicación.
- Separación entre API y lógica de negocio.
- Uso de un servicio especializado para atender las solicitudes.
- Arquitectura preparada para incorporar nuevos endpoints sin modificar otros módulos.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Router Organizations | Implementado |
| Endpoint GET | Implementado |
| Integración con Services | Implementado |
| Versionamiento API | Implementado |
---

## 11.5 Archivo `organization_service.py`

**Ubicación**

```text
backend/app/services/organization_service.py
```

### Propósito

El archivo `organization_service.py` implementa la capa de servicios del módulo de Organizaciones.

Su responsabilidad es coordinar la ejecución de los casos de uso relacionados con las organizaciones, actuando como intermediario entre la API REST y la capa de persistencia.

Actualmente la lógica de negocio es mínima, delegando completamente la consulta al repositorio correspondiente.

---

### Responsabilidades

Actualmente el servicio realiza las siguientes funciones:

- Instanciar el repositorio de organizaciones.
- Exponer los casos de uso del módulo.
- Delegar las operaciones de acceso a datos al repositorio.

En futuras versiones, esta capa será el lugar donde se implementarán las reglas de negocio del módulo.

---

### Repositorio Asociado

El servicio utiliza una instancia de:

```text
OrganizationRepository
```

Toda operación relacionada con la persistencia de organizaciones deberá realizarse mediante este repositorio.

---

### Caso de Uso Implementado

Actualmente existe un único caso de uso.

| Método | Descripción |
|---------|-------------|
| get_all() | Obtiene todas las organizaciones registradas |

La implementación delega completamente la operación al repositorio.

---

### Flujo de Ejecución

```text
API

↓

OrganizationService

↓

OrganizationRepository

↓

Base de Datos
```

El servicio desacopla la API de la implementación de persistencia.

---

### Dependencias

El archivo depende de:

- OrganizationRepository.

No interactúa directamente con SQLAlchemy ni con la configuración de la base de datos.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- Existe una capa de servicios independiente.
- La lógica de negocio queda desacoplada de la API.
- El acceso a datos se realiza exclusivamente mediante repositorios.
- La estructura facilita la incorporación de nuevas reglas de negocio sin modificar los controladores.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Service Layer | Implementado |
| Integración con Repository | Implementado |
| Caso de uso `get_all()` | Implementado |
---

## 11.6 Archivo `organization_repository.py`

**Ubicación**

```text
backend/app/repositories/organization_repository.py
```

### Propósito

El archivo `organization_repository.py` implementa la capa de acceso a datos del módulo de Organizaciones.

Su responsabilidad es encapsular las operaciones relacionadas con la obtención y persistencia de información, evitando que la capa de servicios conozca los detalles de almacenamiento.

En la implementación actual, el repositorio devuelve un conjunto de datos estático utilizado como información de prueba durante las primeras etapas del desarrollo.

---

### Responsabilidades

Actualmente el repositorio realiza las siguientes funciones:

- Proporcionar el método `get_all()`.
- Retornar una colección de organizaciones.
- Actuar como punto de acceso a los datos del módulo.

En futuras versiones este componente será responsable de ejecutar consultas sobre PostgreSQL mediante SQLAlchemy.

---

### Implementación Actual

El método implementado es:

| Método | Descripción |
|---------|-------------|
| `get_all()` | Retorna una lista de organizaciones de prueba |

Actualmente la información retornada corresponde a un registro simulado.

```json
[
  {
    "id": 1,
    "name": "CelebraWeb Demo",
    "country": "Colombia",
    "status": "ACTIVE"
  }
]
```

Esta implementación permite validar el funcionamiento completo del flujo:

API → Service → Repository

sin depender todavía de una base de datos operativa.

---

### Flujo de Ejecución

```text
Solicitud HTTP

↓

Organizations API

↓

OrganizationService

↓

OrganizationRepository

↓

Datos de prueba

↓

Respuesta JSON
```

---

### Dependencias

Actualmente el repositorio no posee dependencias externas.

No utiliza todavía:

- SQLAlchemy.
- SessionLocal.
- Modelos.
- Consultas SQL.

Su implementación corresponde a un repositorio simulado (Mock Repository) utilizado durante el desarrollo inicial.

---

### Observaciones de Arquitectura

Durante la auditoría del Sprint 2 se identifican las siguientes decisiones arquitectónicas:

- La arquitectura desacopla completamente el acceso a datos de la lógica de negocio.
- El uso de datos simulados permitió validar el funcionamiento de toda la arquitectura antes de integrar la persistencia real.
- La transición hacia PostgreSQL podrá realizarse modificando únicamente esta capa, sin afectar la API ni los servicios.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Repository Pattern | Implementado |
| Método `get_all()` | Implementado |
| Datos simulados | Implementado |
| Integración con Base de Datos | Pendiente |
---

# 12. Historial de Implementación

Este capítulo registra la evolución técnica de CelebraWeb.

Su objetivo es mantener la trazabilidad de los cambios realizados en cada Sprint sin duplicar la documentación técnica de los componentes.

La descripción funcional y técnica del software siempre corresponderá al estado actual de la plataforma. El historial únicamente registrará cuándo fueron incorporadas las funcionalidades.

---

## Sprint 1

### Objetivo

Construcción de la arquitectura base del backend.

### Componentes implementados

- Inicialización del proyecto.
- Configuración de FastAPI.
- Organización del repositorio.
- Configuración de SQLAlchemy.
- Configuración de conexión a base de datos.
- Definición de la clase Base para los modelos.
- Definición de la arquitectura por capas.

### Resultado

Se estableció la infraestructura técnica sobre la cual evolucionará la plataforma.

---

## Sprint 2

### Objetivo

Implementación del primer módulo funcional.

### Componentes implementados

- Router Organizations.
- Organization Service.
- Organization Repository.
- Primer endpoint REST.
- Flujo completo API → Service → Repository.

### Resultado

Se validó la arquitectura completa mediante la implementación del primer caso de uso.

Actualmente el repositorio utiliza información simulada para validar el funcionamiento del flujo antes de integrar la persistencia definitiva.


El siguiente Sprint estará orientado a completar la integración entre el Backend y PostgreSQL ejecutando toda la infraestructura de desarrollo dentro de Docker, iniciando posteriormente la persistencia real mediante SQLAlchemy y Alembic.
---

## Sprint 3

### Objetivo

Consolidar la infraestructura base del backend Enterprise de CelebraWeb y validar la arquitectura tecnológica para soportar el desarrollo de la plataforma.

### Componentes implementados

- Configuración completa del entorno de desarrollo.
- Integración de Docker con PostgreSQL 17 y Redis 7.
- Configuración de variables de entorno mediante `.env`.
- Implementación del mecanismo de inyección de dependencias (`get_db()`).
- Configuración de SQLAlchemy para la persistencia.
- Validación de Swagger / OpenAPI.
- Validación de la arquitectura por capas.
- Auditoría técnica de la infraestructura.

### Resultado

Se confirmó la solidez de la arquitectura del backend y de la infraestructura base del proyecto.

Durante las pruebas de integración se identificó una incompatibilidad entre Python ejecutándose directamente sobre Windows y PostgreSQL ejecutándose dentro de Docker.

Después de una auditoría técnica se descartaron problemas de configuración en FastAPI, SQLAlchemy, PostgreSQL, Docker, Redis, variables de entorno y conectividad de red.

Como resultado se tomó la decisión arquitectónica de ejecutar el Backend de CelebraWeb directamente dentro de Docker, alineando el entorno de desarrollo con el entorno de producción y garantizando mayor estabilidad para las siguientes etapas del proyecto.

---

## Sprint 4 – Fase 1

### Objetivo

Migrar el entorno de ejecución del backend desde un entorno híbrido (Python en Windows + PostgreSQL en Docker) hacia una arquitectura completamente contenerizada mediante Docker Compose.

---

### Motivación

Durante la validación del Sprint 3 se identificó un problema persistente de conectividad entre el backend ejecutado en Windows y PostgreSQL ejecutado dentro de Docker.

Después de una auditoría técnica se concluyó que la infraestructura de PostgreSQL funcionaba correctamente y que el inconveniente estaba asociado al entorno de ejecución híbrido.

Como decisión de arquitectura se estableció que todo el backend se ejecutará dentro de Docker, manteniendo un entorno homogéneo para desarrollo, pruebas y producción.

---

### Componentes implementados

- Dockerfile para el Backend FastAPI.
- Integración del Backend en Docker Compose.
- Configuración compartida mediante archivo `.env`.
- Comunicación interna Backend → PostgreSQL.
- Comunicación interna Backend → Redis.
- Publicación del servicio FastAPI en el puerto 8000.
- Publicación de la documentación Swagger/OpenAPI.

---

### Validaciones realizadas

Se validó correctamente el siguiente flujo:

```
Swagger

↓

FastAPI

↓

API REST

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy

↓

PostgreSQL Docker
```

Durante la ejecución del endpoint `GET /api/v1/organizations/`, PostgreSQL respondió correctamente a la consulta realizada por SQLAlchemy.

El error obtenido correspondió a:

```
relation "organizations" does not exist
```

Lo anterior confirma que:

- La comunicación entre el Backend y PostgreSQL funciona correctamente.
- SQLAlchemy ejecuta consultas correctamente.
- La infraestructura Docker quedó validada.
- El siguiente paso corresponde únicamente a la creación del esquema de base de datos mediante Alembic.

---

### Resultado del Sprint

Se completó satisfactoriamente la migración de la infraestructura hacia Docker.

La plataforma dispone ahora de un entorno de desarrollo alineado con la arquitectura objetivo de producción.

---

### Estado de Implementación

| Componente | Estado |
|------------|--------|
| Docker Backend | Implementado |
| Docker Compose | Implementado |
| PostgreSQL | Implementado |
| Redis | Implementado |
| SQLAlchemy | Implementado |
| Swagger | Implementado |
| Comunicación Backend → PostgreSQL | Validada |
| Migraciones Alembic | Pendiente |
| Esquema de Base de Datos | Pendiente |



### Lecciones Aprendidas

- Validar primero la infraestructura antes de desarrollar funcionalidades.
- Mantener sincronizados código y documentación.
- Documentar las decisiones de arquitectura inmediatamente después de ser aprobadas.
- Priorizar soluciones arquitectónicas sobre soluciones específicas del entorno local.

Los siguientes Sprint deberán enfocarse en:

1. Dockerizar completamente el Backend.
2. Integrar PostgreSQL mediante SQLAlchemy.
3. Configurar Alembic y las primeras migraciones.
4. Implementar la persistencia real del módulo Organizations.
5. Continuar el desarrollo de los módulos funcionales de la plataforma.
6. Mantener sincronizada la documentación técnica con cada Sprint.
# 13. Estado General del Proyecto

## Arquitectura

| Componente | Estado |
|------------|--------|
| Arquitectura por capas | Implementado |
| Repository Pattern | Implementado |
| Service Layer | Implementado |
| API REST | Implementado |

---

## Infraestructura

| Componente | Estado |
|------------|--------|
| FastAPI | Implementado |
| SQLAlchemy | Implementado |
| PostgreSQL | Configurado |
| Docker | Configurado |

---

## Backend

| Componente | Estado |
|------------|--------|
| Organización del proyecto | Implementado |
| Organización (Módulo) | Implementado |
| Endpoint GET | Implementado |

---

## Frontend

| Componente | Estado |
|------------|--------|
| Frontend Web | Pendiente |

---

## Módulos de Negocio

| Módulo | Estado |
|---------|--------|
| Organizations | Implementado |
| Users | Pendiente |
| Workspaces | Pendiente |
| Experiences | Pendiente |
| Guests | Pendiente |
| RSVP | Pendiente |
| Check-In | Pendiente |
| Communications | Pendiente |
| Finance | Pendiente |
| Analytics | Pendiente |

---

# 14. Próximos Pasos

Con la finalización del Sprint 2, la plataforma dispone de una base arquitectónica estable.

Los siguientes Sprint deberán enfocarse en:

1. Consolidar la persistencia real mediante PostgreSQL.
2. Incorporar nuevos módulos funcionales.
3. Implementar autenticación y autorización.
4. Desarrollar el frontend de la plataforma.
5. Mantener actualizado este documento conforme evolucione el software.

---

# Control de Versiones del Handbook

| Versión | Fecha | Descripción |
|----------|-------|-------------|
| 1.0.0 | 30-06-2026 | Primera versión del Engineering Handbook. Documenta la arquitectura y la implementación correspondiente a los Sprint 1 y Sprint 2. |

| Versión | Fecha      | Descripción |
| ------- | ---------- | ----------- |
| 1.0.0   | 30-06-2026 | ...         |

| Versión   | Fecha          | Descripción                                                                                                                                                                                                           |
| Versión   | Fecha          | Descripción                                                                                                                                                                                                           |
| --------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.1.0** | **30-06-2026** | **Actualización correspondiente al cierre del Sprint 3. Se documenta la validación de la infraestructura base, la auditoría técnica realizada y la decisión arquitectónica de ejecutar el Backend dentro de Docker.** |

# 15. PMO

<!-- PMO:START -->


## Estado del Proyecto

Proyecto : CelebraWeb Platform

Versión : 0.2.0

Release : 0.2.0

Fase : Foundation

Sprint : 9

Nombre Sprint : Sprint 9

Estado : Closed

Última actualización automática por CW PMO.


<!-- PMO:END -->

