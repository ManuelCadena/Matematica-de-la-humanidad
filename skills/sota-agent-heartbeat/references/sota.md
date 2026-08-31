# Why this stack (2025–2026)

Load only when you must defend the design. Not needed to register
a session.

## Three layers

1. `AGENTS.md` — OpenAI 2025, donated to AAIF / Linux Foundation
   with MCP and goose. Markdown, no schema. Short files win.
   Bloated root files raise cost and are a documented smell
   (Context Bloat).
2. `SKILL.md` — agentskills.io. Progressive disclosure
   (name+description, then body, then scripts/assets).
3. Provenance — W3C PROV (Agent / Activity / Entity). Runtime
   cousins are PROV-AGENT + MCP observability and OTel GenAI
   spans. Those need a collector. This skill does not.

## What v1.1 adds on top of that SOTA

Generic agent stacks record that an agent wrote a file.
They do not record whether a declared count matches `meta`,
or whether a domain invariant still holds.

| Piece | Covers | Extra |
|---|---|---|
| claimed vs attested + hashes | explicit provenance; claimed-vs-attested identity | counts measured from disk |
| session sha256 chain | hashed ledger, cut down | editor-only integrity |
| config-driven invariants | instruction files compiled to checks | domain-specific, not hardcoded |
| typed roles + evidence | typed memory; evidence tracing | works on handbooks, not tool traces |

## Deliberately out of scope

Collector, DID/VC, RDF/PROV-O, cryptographic ledgers.
Add them only when the user asks for infrastructure.

## What this skill is not

It is not equivalent to a PROV-AGENT runtime, an OTel backend,
or a git hook. It is an aligned subset of that SOTA plus four
checks that those stacks leave to the application: measured
counts, file hashes, a session chain, and executable invariants.
