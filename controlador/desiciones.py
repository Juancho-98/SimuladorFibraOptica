"""
Módulo: desiciones.py
Responsable: Scarlett
Función: Árbol de decisión y evaluación de viabilidad técnica del enlace (RF-06).
"""

from typing import Dict, Any


def evaluar_viabilidad(
    p_rx_dbm: float,
    s_rx_dbm: float,
    p_sat_dbm: float,
    margen_diseno_db: float = 3.0
) -> Dict[str, Any]:
    """Implementa el árbol de decisión técnico de 4 estados establecido en RF-06."""
    margen_db = round(p_rx_dbm - s_rx_dbm, 4)

    if p_rx_dbm > p_sat_dbm:
        atenuacion_req = round(p_rx_dbm - p_sat_dbm + 1.0, 2)
        return {
            "estado": "NO VIABLE (Saturación)",
            "viable": False,
            "margen_db": margen_db,
            "diagnostico": f"Potencia recibida ({p_rx_dbm:.2f} dBm) excede el nivel de saturación ({p_sat_dbm:.2f} dBm).",
            "recomendacion": f"Instalar un atenuador óptico fijo de al menos {atenuacion_req} dB en el receptor."
        }
    elif margen_db < 0:
        deficit = round(abs(margen_db), 2)
        return {
            "estado": "NO VIABLE (Atenuación)",
            "viable": False,
            "margen_db": margen_db,
            "diagnostico": f"Señal por debajo de la sensibilidad mínima por {deficit} dB (BER inaceptable).",
            "recomendacion": "Incrementar P_tx, utilizar receptor APD de mayor sensibilidad o reducir pérdidas pasivas."
        }
    elif margen_db < margen_diseno_db:
        return {
            "estado": "CRÍTICO / EN RIESGO",
            "viable": True,
            "margen_db": margen_db,
            "diagnostico": f"Enlace operativo pero con margen ({margen_db:.2f} dB) inferior al recomendado ({margen_diseno_db:.2f} dB).",
            "recomendacion": "Considerar fibra de menor atenuación (ej. UIT-T G.652.D a 1550 nm) para reserva por envejecimiento."
        }
    else:
        return {
            "estado": "VIABLE Y ÓPTIMO",
            "viable": True,
            "margen_db": margen_db,
            "diagnostico": f"Enlace cumple sensibilidad con margen de seguridad positivo de {margen_db:.2f} dB.",
            "recomendacion": "Diseño aprobado dentro de parámetros normativos ITU-T / TIA-568."
        }