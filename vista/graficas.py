"""
Módulo: graficas.py
Responsable: Integrante 6
Función: Renderización de curvas de perfil de potencia óptica en Plotly (RF-08).
"""

import numpy as np
import plotly.graph_objects as go


def crear_grafica_perfil_potencia(
    z_km: np.ndarray,
    potencia_dbm: np.ndarray,
    s_rx_dbm: float,
    p_sat_dbm: float
) -> go.Figure:
    """Genera el gráfico interactivo de decaimiento de potencia vs distancia (RF-08)."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=z_km,
        y=potencia_dbm,
        mode="lines",
        name="Potencia Óptica P(z)",
        line=dict(color="#1A365D", width=3)
    ))

    fig.add_hline(
        y=s_rx_dbm,
        line_dash="dash",
        line_color="#E53E3E",
        annotation_text=f"Sensibilidad Mínima Srx ({s_rx_dbm} dBm)",
        annotation_position="bottom right"
    )

    fig.add_hline(
        y=p_sat_dbm,
        line_dash="dot",
        line_color="#DD6B20",
        annotation_text=f"Nivel de Saturación Psat ({p_sat_dbm} dBm)",
        annotation_position="top right"
    )

    fig.update_layout(
        title="Perfil Espacial de Presupuesto de Potencia Óptica",
        xaxis_title="Distancia del Enlace z (km)",
        yaxis_title="Nivel de Potencia Óptica (dBm)",
        template="plotly_white",
        hovermode="x unified"
    )
    return fig