# SOTA — documentación de ecosistemas agénticos (2025–2026)

Leer solo si hay que justificar el diseño. No hace falta para registrar una sesión.

## Tres capas que no se mezclan

1. **Instrucción de proyecto** — `AGENTS.md`
   - Lanzado por OpenAI ago 2025, donado a la Agentic AI Foundation (Linux Foundation) dic 2025 junto con MCP y goose.
   - ~97 000 archivos raíz en GitHub a jun 2026.
   - Markdown plano, sin schema. ToC de ~100 líneas. ETH Zurich: un AGENTS.md estilo README enciclopédico baja rendimiento 2–3 % y sube costo >20 %.
   - Equivalentes: `CLAUDE.md`, `.github/copilot-instructions.md`, legado `.cursorrules`.
   - Convención de este repo: `AGENTS.md` apunta; `LLM.md` manda.

2. **Capacidad portable** — `SKILL.md` (agentskills.io)
   - Anthropic oct 2025; Cursor 2.4 (ene 2026); Codex CLI; Gemini CLI.
   - Frontmatter obligatorio: `name`, `description`. Progressive disclosure en 3 niveles.
   - Agent Plugins 1.0 (ago 2026: Amazon, Anysphere, Microsoft, OpenAI, Vercel) empaqueta skills + MCP.
   - Este oficio es un skill, no un párrafo más en AGENTS.md.

3. **Provenance / observabilidad**
   - W3C PROV: Agent / Activity / Entity / used / generated.
   - Keep a Changelog + SemVer para *versiones de corpus*.
   - OpenTelemetry GenAI (en desarrollo): `invoke_agent`, `gen_ai.agent.id`, `gen_ai.conversation.id`. Útil en runtime, pesado para un repo de conocimiento.
   - AIGP / Agent Assurance: Merkle + políticas. Exceso para este corpus.

El heartbeat es la proyección PROV-lite de la capa 3 sobre git.

## Verificación Consensus — 2026-08-30

Consulta MCP a >220 M de papers. No cambia el diseño; documenta el piso.

- Souza et al. 2025, IEEE eScience (*PROV-AGENT*): W3C PROV + MCP es el
  primo académico más cercano. Nuestro log es la proyección markdown
  de Agent/Activity/Entity, no el collector runtime.
- Hu et al. 2026 (*Responsible Agentic AI Requires Explicit Provenance*):
  provenance explícito es condición necesaria, no refinamiento opcional.
- Xu et al. 2026 (*Agent Skills…*): SKILL.md + progressive disclosure
  es la capa de abstracción emergente. Nuestro skill cumple el contrato.
- Gloaguen et al. 2026; Santos et al. 2026: AGENTS.md no mejora success
  rate de forma general y huele a Context Bloat si se infla. ToC corto
  (este repo: 49 líneas) es la práctica soportada.
- Balusu 2026 (*AgentTelemetry*): OTel GenAI cubre invoke/tool, no
  planning/reasoning/memory/delegation. No usarlo como pulso de corpus.
- Staufer et al. 2026 FAccT (*2025 AI Agent Index*): la mayoría de
  agentes desplegados documentan mal safety/eval. Registrar sesión
  es la excepción, no la norma.

Veredicto interno: `aligned-subset`. No reivindicar equivalencia con
PROV-AGENT, ProvenanceGuard, AgentTrace o ledgers criptográficos.

## v1.1 — cómo se mejora el SOTA sin collector (2026-08-31)

El SOTA genérico rastrea *que un agente escribió un archivo*. Este
corpus necesita *que el número declarado sea el del `meta` y que
Teotihuacan no sobreviva a t=700*. Eso no lo da AGENTS.md ni OTel GenAI.

| Pieza v1.1 | SOTA que cubre | Paso más allá |
|---|---|---|
| `attestation.measured` + hashes | Hu 2026 explicit provenance; LDP claimed-vs-attested | atestación de *conteos históricos*, no de calidad del modelo |
| `chain.prev_sha256` | Traccia hashed ledger (recortado) | integridad append-only con editor de texto |
| invariantes en el validador | ContextCov: instrucciones → guardrails | guardrails de historiografía (cono datado, capa 0.5 ≠ Estado) |
| `role` en used/generated | MemIR typed memory | evita colapso evidencia/claim *en el log de sesión* |
| Evidence en mutaciones | Wang 2026 evidence tracing | aplicado a handbooks, no a tool traces |

## Lo que deliberadamente no adoptamos

- Collector OTel (no hay backend).
- Un `AGENTS.md` de 2 000 líneas.
- Un changelog por commit de git (git ya existe).
- Transcripts de chat como log.
