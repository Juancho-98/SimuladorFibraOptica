"""
Módulo: validaciones.py
Responsable: Scarlett
Función: Estructura de datos y validación física de entradas (RF-01 / RNF-03).
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class ParametrosEnlace:
    """Estructura de datos de entrada para un enlace óptico punto a punto."""
    longitud_km: float
    longitud_onda_nm: int
    tipo_fibra: str
    atenuacion_db_km: float
    p_tx_dbm: float
    s_rx_dbm: float
    p_sat_dbm: float = 0.0
    n_empalmes_fusion: int = 0
    perdida_fusion_db: float = 0.05
    n_empalmes_mecanicos: int = 0
    perdida_mecanica_db: float = 0.30
    n_conectores: int = 2
    perdida_conector_db: float = 0.75
    margen_diseno_db: float = 3.0

    def validar(self) -> Tuple[bool, str]:
        """Valida restricciones físicas y dimensionales antes del cálculo."""
        if self.longitud_km <= 0:
            return False, "Error (RF-01): La longitud del enlace debe ser mayor a 0 km."
        if not (800 <= self.longitud_onda_nm <= 1650):
            return False, "Error (RF-01): La longitud de onda debe estar en el rango comercial [800, 1650] nm."
        if self.atenuacion_db_km < 0:
            return False, "Error (RF-01): El coeficiente de atenuación no puede ser negativo."
        if not (-50.0 <= self.p_tx_dbm <= 30.0):
            return False, "Error (RF-01): La potencia del transmisor debe estar entre -50 dBm y +30 dBm."
        if not (-60.0 <= self.s_rx_dbm <= 0.0):
            return False, "Error (RF-01): La sensibilidad del receptor debe estar entre -60 dBm y 0 dBm."
        if self.s_rx_dbm >= self.p_sat_dbm:
            return False, "Error (RF-01): La sensibilidad (S_rx) debe ser estrictamente menor al nivel de saturación (P_sat)."
        if self.n_conectores < 2:
            return False, "Error (RF-01): Un enlace punto a punto requiere al menos 2 conectores (TX y RX)."
        if any(n < 0 for n in [self.n_empalmes_fusion, self.n_empalmes_mecanicos, self.n_conectores]):
            return False, "Error (RF-01): La cantidad de empalmes o conectores no puede ser negativa."
        if any(p < 0 for p in [self.perdida_fusion_db, self.perdida_mecanica_db, self.perdida_conector_db]):
            return False, "Error (RF-01): Las pérdidas unitarias de inserción no pueden ser negativas."
        if self.margen_diseno_db < 0:
            return False, "Error (RF-01): El margen de diseño recomendado no puede ser negativo."
        return True, "Parámetros validados correctamente."