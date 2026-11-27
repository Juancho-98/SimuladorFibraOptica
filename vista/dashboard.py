"""
Módulo: dashboard.py
Responsable: Integrante 5
Función: Tarjetas de indicadores clave (KPIs) y resultados en el panel central.
"""

import streamlit as st
from typing import Dict, Any


def renderizar_tarjetas_kpi(res_potencia: Dict[str, Any], veredicto: Dict[str, Any]) -> None:
    """Despliega las tarjetas principales de resultados en el panel central."""
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Pérdida Total (Atotal)", f"{res_potencia['perdida_total_db']} dB")
    col2.metric("Potencia Recibida (Prx)", f"{res_potencia['p_rx_dbm']} dBm")
    col3.metric("Margen de Seguridad (M)", f"{res_potencia['margen_seguridad_db']} dB")
    col4.metric("Estado del Enlace", veredicto["estado"])