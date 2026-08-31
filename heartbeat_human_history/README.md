# Heartbeat of Human History

Protocolo de **estatus + bitácora** para cualquier modelo o humano que
toque este repositorio. Versión de contrato: **heartbeat.v1.1**.

No sustituye a git. No es OpenTelemetry. Es el pulso que un agente
puede leer en frío y el registro que **debe** dejar al irse.

Si eres un modelo: este archivo + `../LLM.md` + `../AGENTS.md`.
Si no registras la sesión, el trabajo no cuenta como parte del corpus.

---

## Por qué existe

En 2025–2026 el ecosistema agéntico se partió en tres capas:

| Capa | Estándar | Qué resuelve | Qué no |
|---|---|---|---|
| Instrucción de proyecto | `AGENTS.md` (AAIF / Linux Foundation) | orientación corta | historial |
| Capacidad portable | `SKILL.md` (agentskills.io) | cómo hacer un oficio | estado del repo |
| Provenance | W3C PROV + Keep a Changelog + OTel `gen_ai.agent.*` | quién hizo qué a qué | este corpus |

Este directorio cubre la tercera capa **sin** levantar un collector.
Un archivo JSON de pulso + un markdown por sesión. Cualquier LLM
con permiso de escritura puede cumplir el contrato.

Un `AGENTS.md` enciclopédico baja rendimiento y sube costo. El
protocolo vive aquí, no inflado en la raíz.

---

## Qué añade v1.1 (SOTA-compliant + un paso más)

Cumplir el SOTA 2026 es la triple capa de arriba. Mejorarlo, para un
corpus científico sin backend, son cuatro piezas que esos stacks no
atan al objeto de estudio:

1. **Claimed vs attested.** El pulso declara conteos (`corpus`). El
   validador los *mide* otra vez (`attestation.measured`) y firma
   `sha256` de cada JSON. Un número que el agente recuerda no cuenta.
   (Respuesta al *provenance paradox*: lo auto-declarado no se usa
   para decidir estado.)
2. **Cadena append-only.** Cada sesión apunta a `prev_session_id` +
   `prev_sha256` del markdown anterior. Reescribir un log viejo rompe
   la cadena. No es un ledger con Merkle de runtime; es integridad
   verificable con un editor de texto.
3. **Invariantes ejecutables.** Teotihuacan = `[-100, 650]` y apagada
   en t=700. `species|site|migration|admixture` no comparte `id` con
   un cono político. El validador las corre; no son un checklist
   decorativo.
4. **Roles tipados + evidencia.** `used` / `generated` llevan
   `role`. Una sesión `add-node|add-origin|fix-date|add-cone` exige
   fuente. Eso es evidence-tracing aplicado a historiografía, no a
   traces de tools.

Lo que **no** adoptamos, a propósito: collector OTel, DID/VC,
RDF/PROV-O, ledger criptográfico. No hay backend. El isomorfismo
PROV basta para proyectar después.

---

## Contrato (obligatorio)

Antes de declarar una sesión terminada:

1. Leer `HEARTBEAT.json` (estado actual).
2. Hacer el trabajo siguiendo `LLM.md`.
3. Copiar `../skills/heartbeat-human-history/assets/session.template.md`
   a `log/YYYY-MM-DD_<slug>.md` y llenarlo (incluye `chain` y roles).
4. Añadir una línea al tope de `log/INDEX.md`.
5. Medir, no recordar:

   ```
   python skills/heartbeat-human-history/scripts/validate_heartbeat.py --write-attestation
   ```

6. Reescribir `HEARTBEAT.json` (`schema=heartbeat.v1.1`, `t`,
   `last_session`, `corpus` = measured, `attestation`, `chain`,
   `pending`).
7. Si el cambio es una **versión de corpus**, entrada en `CHANGELOG.md`.
8. Correr el validador sin flags. Exit 0.

Una sesión sin log es una sesión que el siguiente modelo no puede auditar.

---

## Mapa

```
heartbeat_human_history/
  README.md                 este protocolo
  HEARTBEAT.json            pulso (claimed cache + attestation)
  heartbeat.schema.json     contrato draft-07 (v1 y v1.1)
  CHANGELOG.md              versiones del corpus
  log/INDEX.md              índice, más reciente arriba
  log/YYYY-MM-DD_slug.md    una sesión = un archivo
```

Skill portable (progressive disclosure):

```
skills/heartbeat-human-history/SKILL.md
```

---

## Semántica PROV (reducida)

Cada sesión es una **Activity**. El modelo es el **Agent**.
Los JSON/md tocados son **Entities**.

| Campo de la sesión | PROV |
|---|---|
| `agent` | `prov:Agent` |
| `activity.type` | `prov:Activity` |
| `used` + `role` | `prov:used` + tipo |
| `generated` + `role` | `prov:generated` + tipo |
| `started` / `ended` | `prov:startedAtTime` / `endedAtTime` |
| `derived_from` / `chain` | `prov:wasDerivedFrom` / `wasInformedBy` |
| `attestation.hashes` | integridad de Entity |

No exportamos RDF.

---

## Status

`ok` · `degraded` · `diverged` · `blocked`

`degraded` es el estado honesto cuando el workspace está más
adelante que GitHub. No lo pintes `ok` para quedar bien.
`diverged` si `corpus` ≠ `attestation.measured` o un hash no calza.

---

## Qué no registrar

- Transcripciones de chat.
- Secretos, tokens, rutas locales de la máquina del usuario.
- Opiniones sobre el usuario.
- Conteos inventados. Lee `meta` del JSON o `--write-attestation`.

---

## Cómo comprobar

```
python skills/heartbeat-human-history/scripts/validate_heartbeat.py
```

Debe salir `heartbeat ok`. Exit 2 = diverged.
