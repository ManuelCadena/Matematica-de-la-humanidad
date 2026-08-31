# referencia_modelos.py
# Algoritmos canónicos del Modelo Matemático de la Humanidad.
# Copiar / adaptar. No depende de archivos externos salvo que el llamador los cargue.
from __future__ import annotations

from collections import deque
from typing import Iterable

D = ("politico", "historico", "religioso", "cientifico", "cultural", "social")

ADJ = {
    "am-north": ["meso"],
    "meso": ["am-north", "andes"],
    "andes": ["meso"],
    "af-west": ["maghreb", "af-nile", "af-cs"],
    "af-nile": ["af-west", "af-cs", "maghreb", "near-east"],
    "af-cs": ["af-west", "af-nile"],
    "maghreb": ["af-west", "af-nile", "eu-west", "near-east"],
    "eu-west": ["eu-east", "maghreb", "near-east"],
    "eu-east": ["eu-west", "near-east", "iran-steppe"],
    "near-east": ["eu-west", "eu-east", "maghreb", "af-nile", "iran-steppe"],
    "iran-steppe": ["near-east", "eu-east", "sasia", "easia"],
    "sasia": ["iran-steppe", "easia", "seasia"],
    "easia": ["sasia", "iran-steppe", "seasia"],
    "seasia": ["sasia", "easia", "oceania"],
    "oceania": ["seasia"],
    "humanidad": [],
}

KIND_DIM = {
    "polity": "politico", "empire": "politico", "dynasty": "politico",
    "nation": "politico", "colony": "politico", "city-state": "politico",
    "khanate": "politico", "caliphate": "politico", "sultanate": "politico",
    "confederation": "politico", "civilization": "politico",
    "war": "historico", "treaty": "historico", "event": "historico",
    "religion": "religioso", "denomination": "religioso", "canon": "religioso",
    "council": "religioso", "rite": "religioso", "cosmology": "religioso",
    "order": "religioso",
    "species": "cientifico", "climate": "cientifico", "invention": "cientifico",
    "pandemic": "cientifico",
    "culture": "cultural", "text": "cultural", "school": "cultural", "site": "cultural",
    "person": "historico", "migration": "social",
}

SYMMETRIC_TYPES = {
    "exchange", "trade", "coexist", "fusion", "translation", "diffusion",
}


def assign_dims(node: dict) -> list[str]:
    dims = set(node.get("lentes") or [])
    k = node.get("kind")
    if k in KIND_DIM:
        dims.add(KIND_DIM[k])
    if not dims:
        dims.add("historico")
    return sorted(dims)


def overlaps(a, b) -> bool:
    if a is None or b is None or None in a or None in b:
        return False
    return not (a[1] < b[0] or b[1] < a[0])


def d_T(a, b):
    if a is None or b is None or None in a or None in b:
        return None
    if overlaps(a, b):
        return 0
    if a[1] < b[0]:
        return b[0] - a[1]
    return a[0] - b[1]


def d_R(ra: str, rb: str) -> int:
    if ra == rb:
        return 0
    if ra == "humanidad" or rb == "humanidad":
        return 1
    q = deque([(ra, 0)])
    seen = {ra}
    while q:
        x, d = q.popleft()
        for y in ADJ.get(x, []):
            if y in seen:
                continue
            if y == rb:
                return d + 1
            seen.add(y)
            q.append((y, d + 1))
    return 3


def d_D(phi: Iterable[str], psi: Iterable[str]) -> int:
    return 0 if set(phi) & set(psi) else 1


def dist_vector(u: dict, v: dict) -> tuple:
    Iu, Iv = (u.get("start"), u.get("end")), (v.get("start"), v.get("end"))
    ru = u.get("region") or "humanidad"
    rv = v.get("region") or "humanidad"
    return (d_T(Iu, Iv), d_R(ru, rv), d_D(assign_dims(u), assign_dims(v)))


def scalar_dist(vec, alpha, beta, gamma) -> float:
    """Requiere pesos explícitos. No es la métrica del modelo."""
    dt, dr, dd = vec
    dt = 0 if dt is None else dt
    return alpha * dt + beta * dr + gamma * dd


def allen(a, b):
    if a is None or b is None or None in a or None in b:
        return None
    a0, a1 = a
    b0, b1 = b
    if a1 < b0:
        return "meets" if a1 + 1 == b0 else "precedes"
    if b1 < a0:
        return "met_by" if b1 + 1 == a0 else "preceded_by"
    if a0 == b0 and a1 == b1:
        return "equals"
    if a0 == b0 and a1 < b1:
        return "starts"
    if a0 == b0 and a1 > b1:
        return "started_by"
    if a1 == b1 and a0 > b0:
        return "finishes"
    if a1 == b1 and a0 < b0:
        return "finished_by"
    if a0 > b0 and a1 < b1:
        return "during"
    if a0 < b0 and a1 > b1:
        return "contains"
    if a0 < b0 < a1 < b1:
        return "overlaps"
    if b0 < a0 < b1 < a1:
        return "overlapped_by"
    return "overlaps"


def slice_t(nodes: dict, t: int) -> list:
    return [n for n in nodes.values() if n.get("start") is not None
            and n.get("end") is not None and n["start"] <= t <= n["end"]]


def join(acoples: list, ci: str, cj: str, t: int) -> list:
    out = []
    for e in acoples:
        ends = {e["from"], e["to"]}
        if ci not in ends or cj not in ends:
            continue
        I = e["interval"]
        if I["t0"] <= t <= I["t1"]:
            out.append(e)
    return out


def envelope(t: float, t0: float, t1: float, rise: float = 40, fall: float = 40) -> float:
    if t < t0 or t > t1:
        return 0.0
    if t < t0 + rise:
        return max(0.0, (t - t0) / float(rise))
    if t > t1 - fall:
        return max(0.0, (t1 - t) / float(max(1.0, fall)))
    return 1.0


def cone_z(lon, lat, clon, clat, H, R):
    d = ((lon - clon) ** 2 + (lat - clat) ** 2) ** 0.5
    return H * max(0.0, 1.0 - d / max(R, 1e-6))


def phi_at(t, conos, lon, lat, alpha_deg=52.0, hmax=16.0, amp_min=0.04):
    from math import tan, radians
    k = tan(radians(alpha_deg))
    total = 0.0
    active = []
    for c in conos:
        amp = c["peak"] * envelope(t, c["t0"], c["t1"])
        if amp < amp_min:
            continue
        H = amp * hmax
        R = max(5.5, H * k)
        total += cone_z(lon, lat, c["xy"][0], c["xy"][1], H, R)
        active.append(c["id"])
    return total, active


def selftest():
    assert allen((0, 10), (11, 20)) == "meets"
    assert allen((0, 10), (20, 30)) == "precedes"
    assert allen((0, 10), (0, 10)) == "equals"
    assert d_R("af-nile", "near-east") == 1
    assert d_R("andes", "iran-steppe") >= 2
    assert envelope(700, -100, 650) == 0.0
    assert envelope(100, -100, 650) == 1.0
    assert envelope(1400, 1325, 1521) == 1.0
    assert envelope(100, 1325, 1521) == 0.0
    print("selftest ok")


if __name__ == "__main__":
    selftest()
