"""
Función: Estructura estandarizada de resultados numéricos del motor matemático.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class ResultadoSimulacion:
    """Contenedor estructurado de las métricas calculadas por el Modelo."""
    atenuacion_fibra_db: float
    perdidas_eventos_db: float
    perdida_total_db: float
    p_rx_dbm: float
    p_rx_mw: float
    margen_seguridad_db: float
    dt_total_ps: float = 0.0
    tasa_max_libre_isi_gbps: float = 0.0
    capacidad_shannon_gbps: float = 0.0

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte los resultados del modelo a diccionario para el controlador."""
        return asdict(self)