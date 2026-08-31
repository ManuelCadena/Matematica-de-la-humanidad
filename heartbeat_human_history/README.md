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
   `sha256` de cada JSON.
2. **Cadena append-only.** Cada sesión apunta a `prev_session_id` +
   `prev_sha256` del markdown anterior.
3. **Invariantes ejecutables.** Teotihuacan = `[-100, 650]` y apagada
   en t=700. `species|site|migration|admixture` no comparte `id` con
   un cono político.
4. **Roles tipados + evidencia.** `used` / `generated` llevan `role`.

Lo que **no** adoptamos, a propósito: collector OTel, DID/VC,
RDF/PROV-O, ledger criptográfico.

---

## Contrato (obligatorio)

1. Leer `HEARTBEAT.json`.
2. Hacer el trabajo siguiendo `LLM.md`.
3. Copiar la plantilla de sesión a `log/YYYY-MM-DD_<slug>.md`.
4. Añadir una línea al tope de `log/INDEX.md`.
5. Medir con `validate_heartbeat.py --write-attestation`.
6. Reescribir `HEARTBEAT.json` (`schema=heartbeat.v1.1`).
7. CHANGELOG si hay versión de corpus.
8. Validador sin flags. Exit 0.

```
python skills/heartbeat-human-history/scripts/validate_heartbeat.py
```
