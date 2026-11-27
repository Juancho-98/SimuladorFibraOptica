"""
Función: Entidad de dominio del enlace físico y sus componentes pasivos.
"""

from dataclasses import dataclass


@dataclass
class EnlaceOptico:
    """Representa la infraestructura física de un enlace óptico punto a punto."""
    longitud_km: float
    tipo_fibra: str
    atenuacion_db_km: float
    n_conectores: int = 2
    perdida_conector_db: float = 0.75
    n_empalmes_fusion: int = 0
    perdida_fusion_db: float = 0.05
    n_empalmes_mecanicos: int = 0
    perdida_mecanica_db: float = 0.30

    def obtener_perdida_pasiva_total(self) -> float:
        """Calcula las pérdidas acumuladas por conectores y empalmes."""
        return round(
            (self.n_conectores * self.perdida_conector_db) +
            (self.n_empalmes_fusion * self.perdida_fusion_db) +
            (self.n_empalmes_mecanicos * self.perdida_mecanica_db),
            4
        )