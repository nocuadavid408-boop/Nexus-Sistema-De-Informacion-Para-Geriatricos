"""
Fechas de los medicamentos: texto legible para mostrar los días en que
se administra cada medicamento.
"""

from datetime import date

MESES_CORTOS = ["ene", "feb", "mar", "abr", "may", "jun",
                "jul", "ago", "sep", "oct", "nov", "dic"]


def _a_fecha(texto: str):
    try:
        return date.fromisoformat(texto.strip())
    except ValueError:
        return None


def _rangos(dias) -> str:
    """[22, 23, 24, 25, 28] -> "22–25, 28" (rangos desde 3 días seguidos)."""
    tramos, inicio = [], 0
    for i in range(1, len(dias) + 1):
        if i == len(dias) or dias[i] != dias[i - 1] + 1:
            tramos.append(dias[inicio:i])
            inicio = i
    textos = []
    for t in tramos:
        textos.extend([f"{t[0]}–{t[-1]}"] if len(t) >= 3 else [str(d) for d in t])
    return ", ".join(textos)


def etiqueta_dias(dia) -> str:
    """Texto corto para mostrar los días: "21, 23 oct 2026 · 2 nov 2026"."""
    dia = (dia or "").strip()
    if not dia:
        return "Todos los días"

    fechas, otros = [], []
    for trozo in dia.split(","):
        trozo = trozo.strip()
        if not trozo:
            continue
        f = _a_fecha(trozo)
        (fechas if f else otros).append(f or trozo)

    grupos = {}
    for f in sorted(fechas):
        grupos.setdefault((f.year, f.month), []).append(f.day)
    partes = [
        f"{_rangos(dias)} {MESES_CORTOS[mes - 1]} {anio}"
        for (anio, mes), dias in grupos.items()
    ]
    if otros:
        partes.append(", ".join(otros))
    return " · ".join(partes)
