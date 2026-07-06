---
id: CW-131
code: CW-131
title: Project Context Contract
version: 1.0.0
status: DRAFT
owner: PMO
type: Architecture Contract
created: 2026-07-05
---

# CW-131 – Project Context Contract

## 1. Propósito

Este documento define el contrato oficial mediante el cual el PMO construye el **Project Context** antes de iniciar cualquier Sprint o Historia Técnica.

El objetivo es garantizar que todas las decisiones de diseño, implementación y evolución del producto se fundamenten exclusivamente en la documentación oficial del proyecto y no en la memoria de una conversación, de una IA o de un desarrollador.

---

# 2. Problema que resuelve

Durante la evolución del proyecto se identificó que validar únicamente la existencia de la documentación no garantiza que su conocimiento sea utilizado durante el desarrollo.

Esto puede producir:

- decisiones inconsistentes;
- duplicidad de soluciones;
- desviaciones respecto al ADN del proyecto;
- pérdida de continuidad entre conversaciones;
- incumplimiento de decisiones previamente aprobadas.

El Project Context elimina ese riesgo.

---

# 3. Principios

El Project Context se rige por los siguientes principios.

## 3.1 Single Source of Truth

Toda la información oficial reside exclusivamente en la documentación del repositorio.

El PMO nunca duplicará ese conocimiento.

---

## 3.2 Documentation First

Toda implementación deberá estar respaldada por documentación oficial.

No se implementarán decisiones basadas únicamente en memoria o conversación.

---

## 3.3 Reuse Before Create

Antes de crear componentes, procesos o documentación, deberá verificarse si ya existen dentro del proyecto.

---

## 3.4 Architecture Driven

La arquitectura existente gobierna la implementación.

Nunca se modificará sin una decisión documentada.

---

# 4. Definición del Project Context

El Project Context es el contexto operativo construido por el PMO para un Sprint específico.

No constituye una nueva fuente de verdad.

Su única función consiste en organizar y poner a disposición el conocimiento oficial necesario para desarrollar un Sprint.

---

# 5. Fuentes oficiales del conocimiento

El Project Context únicamente podrá construirse utilizando información proveniente de:

- PROJECT.yaml
- Foundation
- PROJECT-RULES.md
- Engineering Handbook
- Decision Log
- Sprint Summary
- Sprint Artifacts
- Estado actual del proyecto

No se utilizarán conversaciones anteriores como fuente oficial.

---

# 6. Responsabilidades del PMO

Antes de autorizar un Sprint, el PMO deberá:

- validar la documentación requerida;
- leer la documentación oficial;
- interpretar la documentación;
- identificar reglas activas;
- identificar decisiones vigentes;
- identificar lecciones aprendidas aplicables;
- identificar pendientes heredados;
- construir el contexto operativo;
- presentar un Executive Brief.

---

# 7. Responsabilidades del Project Context

El Project Context deberá responder, como mínimo, las siguientes preguntas:

- ¿Qué proyecto estoy desarrollando?
- ¿Cuál es el objetivo del Sprint?
- ¿Qué documentos gobiernan este Sprint?
- ¿Qué reglas debo respetar?
- ¿Qué decisiones se encuentran vigentes?
- ¿Qué lecciones aprendidas debo aplicar?
- ¿Qué pendientes afectan este Sprint?
- ¿Qué componentes están autorizados para modificarse?

---

# 8. Restricciones

El Project Context:

- no duplica documentación;
- no reemplaza Foundation;
- no reemplaza el Decision Log;
- no reemplaza el Engineering Handbook;
- no reemplaza PROJECT-RULES.

El conocimiento permanece únicamente en su fuente oficial.

---

# 9. Integración con el PMO

El Project Context formará parte del flujo oficial del comando:

START

El flujo oficial será:

1. Validar estructura del proyecto.
2. Validar documentación requerida.
3. Leer documentación oficial.
4. Construir Project Context.
5. Generar Executive Brief.
6. Autorizar el Sprint.

---

# 10. Criterio de autorización

Un Sprint únicamente podrá considerarse listo para desarrollo cuando el PMO confirme que:

- la documentación requerida existe;
- el contexto operativo fue construido;
- las reglas activas fueron identificadas;
- las decisiones vigentes fueron consideradas;
- las lecciones aprendidas fueron incorporadas;
- los pendientes heredados fueron identificados.

---

# 11. Regla de Gobernanza

Toda decisión técnica deberá poder responder la siguiente pregunta:

> ¿Dónde está documentada?

Si la respuesta no puede encontrarse dentro de la documentación oficial del proyecto, la implementación deberá detenerse hasta documentar y aprobar dicha decisión.

---

# 12. Objetivo Estratégico

El propósito final del Project Context consiste en que cualquier IA, desarrollador o integrante del equipo pueda incorporarse al proyecto utilizando exclusivamente la documentación oficial y el contexto construido por el PMO, eliminando la dependencia de la memoria de conversaciones anteriores.