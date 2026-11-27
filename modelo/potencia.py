"""
Módulo: potencia.py
Responsable: Juan
Función: Cálculos de atenuación, pérdidas por eventos y presupuesto de potencia óptica (RF-02 a RF-05).
"""

import numpy as np
from typing import Dict, Any, Tuple


def calcular_atenuacion_fibra(longitud_km: float, atenuacion_db_km: float) -> float:
    """Calcula la pérdida lineal distribuida en la fibra: A_fibra = alpha * L (RF-02)."""
    return round(float(atenuacion_db_km * longitud_km), 4)


def calcular_perdidas_eventos(
    n_empalmes_fusion: int,
    perdida_fusion_db: float,
    n_empalmes_mecanicos: int,
    perdida_mecanica_db: float,
    n_conectores: int,
    perdida_conector_db: float
) -> float:
    """Calcula las pérdidas concentradas por empalmes y conectores (RF-03)."""
    total = (
        (n_empalmes_fusion * perdida_fusion_db) +
        (n_empalmes_mecanicos * perdida_mecanica_db) +
        (n_conectores * perdida_conector_db)
    )
    return round(float(total), 4)


def calcular_balance_potencia(
    longitud_km: float,
    atenuacion_db_km: float,
    p_tx_dbm: float,
    s_rx_dbm: float,
    n_empalmes_fusion: int = 0,
    perdida_fusion_db: float = 0.05,
    n_empalmes_mecanicos: int = 0,
    perdida_mecanica_db: float = 0.30,
    n_conectores: int = 2,
    perdida_conector_db: float = 0.75
) -> Dict[str, Any]:
    """Ejecuta el presupuesto completo de potencia óptica (RF-04 y RF-05)."""
    a_fibra = calcular_atenuacion_fibra(longitud_km, atenuacion_db_km)
    a_eventos = calcular_perdidas_eventos(
        n_empalmes_fusion, perdida_fusion_db,
        n_empalmes_mecanicos, perdida_mecanica_db,
        n_conectores, perdida_conector_db
    )
    a_total = round(a_fibra + a_eventos, 4)
    p_rx_dbm = round(p_tx_dbm - a_total, 4)
    p_rx_mw = float(10 ** (p_rx_dbm / 10.0))
    p_rx_uw = p_rx_mw * 1000.0
    margen_db = round(p_rx_dbm - s_rx_dbm, 4)

    return {
        "atenuacion_fibra_db": a_fibra,
        "perdidas_eventos_db": a_eventos,
        "perdida_total_db": a_total,
        "p_rx_dbm": p_rx_dbm,
        "p_rx_mw": round(p_rx_mw, 6),
        "p_rx_uw": round(p_rx_uw, 3),
        "margen_seguridad_db": margen_db
    }


def generar_perfil_espacial(
    longitud_km: float,
    atenuacion_db_km: float,
    p_tx_dbm: float,
    perdida_conector_db: float,
    n_conectores: int,
    perdida_empalmes_total_db: float,
    puntos: int = 200
) -> Tuple[np.ndarray, np.ndarray]:
    """Genera los vectores z (km) y P(z) (dBm) para el perfil gráfico de potencia (RF-08)."""
    z = np.linspace(0, longitud_km, puntos)
    # Pérdida en conector de transmisión al inicio (z = 0)
    p_inicio = p_tx_dbm - perdida_conector_db
    # Pendiente lineal por atenuación + distribución proporcional de empalmes intermedios
    perdida_intermedia_por_km = perdida_empalmes_total_db / longitud_km if longitud_km > 0 else 0.0
    potencia_z = p_inicio - (atenuacion_db_km + perdida_intermedia_por_km) * z
    # Caída en conector de recepción al final (z = L)
    if n_conectores >= 2:
        potencia_z[-1] -= perdida_conector_db * (n_conectores - 1)
    return z, potencia_z