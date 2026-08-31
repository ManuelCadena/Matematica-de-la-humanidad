#!/usr/bin/env python3
"""Rebuild datos/historia_ontologia.json from shell + nodos jsonl."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
shell = json.loads((root/"datos/historia_ontologia.shell.json").read_text())
nodos = {}
for line in (root/"datos/ontologia_nodos.jsonl").read_text().splitlines():
    if not line.strip():
        continue
    n = json.loads(line)
    nodos[n["id"]] = n
shell["nodos"] = nodos
out = root/"datos/historia_ontologia.json"
out.write_text(json.dumps(shell, ensure_ascii=False, indent=2) + "\n")
print("wrote", out, "n_nodos", len(nodos))
