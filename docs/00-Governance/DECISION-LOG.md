---
id: CW-120
code: CW-120
title: Decision Log
version: 1.1.0
status: APPROVED
classification: INTERNAL

owner: Enterprise Architecture

created: 2026-07-01
updated: 2026-07-03

repository: docs/00-Governance/DECISION-LOG.md

references:
  - PROJECT.yaml
  - CW-110
---

# CW-120 - Decision Log

Registro cronológico de decisiones aprobadas por el Product Owner.

---

## DEC-001

**Fecha:** 2026-07-01

**Título:** El chat no es la memoria del proyecto.

**Decisión**

Toda decisión aprobada debe registrarse inmediatamente en la documentación oficial.

---

## DEC-002

**Fecha:** 2026-07-01

**Título:** El PMO es una herramienta de apoyo.

**Decisión**

El PMO no hace parte de los entregables de CelebraWeb.

Su función es apoyar el desarrollo y mantener la documentación del proyecto.

---

## DEC-003

**Fecha:** 2026-07-01

**Título:** Lectura obligatoria antes del Sprint.

**Decisión**

Antes de iniciar un Sprint el PMO debe leer la documentación oficial del proyecto para reconstruir el contexto y validar el estado antes de permitir el inicio del desarrollo.

---

## DEC-004

**Fecha:** 2026-07-02

**Título:** Automatización de la documentación administrativa del Sprint.

**Decisión**

Se aprueba la incorporación del comando **generate** al CW PMO como mecanismo oficial para generar automáticamente la documentación administrativa del Sprint.

El comando **generate** será responsable de orquestar la generación de los documentos del Sprint reutilizando los servicios existentes del PMO.

Como consecuencia de esta decisión:

- La generación documental deja de depender de ediciones manuales.
- `GenerateService` actuará como orquestador y no contendrá lógica de negocio.
- `SprintCloseCommand` delegará la generación documental en `GenerateService`.
- La gobernanza, el código y la documentación deberán permanecer sincronizados al finalizar cada Sprint.

---

## DEC-005

**Fecha:** 2026-07-03

**Título:** Desarrollo guiado por Arquitectura Empresarial y Enterprise Knowledge System.

**Decisión**

A partir del Sprint 8, el desarrollo de CelebraWeb adoptará oficialmente un enfoque de Arquitectura Empresarial alineado con la Constitución Empresarial (CW-000).

Toda funcionalidad deberá mantener trazabilidad con la arquitectura del producto y con el Enterprise Knowledge System (EKS).

El proceso oficial de construcción del producto seguirá la siguiente secuencia:

Constitución Empresarial

↓

Modelo Empresarial

↓

Dominio Empresarial

↓

Business Capability

↓

Proceso de Negocio

↓

Arquitectura de Software

↓

Implementación

Como consecuencia de esta decisión:

- La Constitución Empresarial constituye la máxima autoridad funcional del producto.
- El Enterprise Knowledge System será la única fuente oficial de conocimiento permanente.
- Las conversaciones se consideran espacios de trabajo y no repositorios oficiales de conocimiento.
- El desarrollo del producto se organizará alrededor de Business Capabilities.
- La arquitectura de software será consecuencia de la arquitectura empresarial y no su punto de partida.