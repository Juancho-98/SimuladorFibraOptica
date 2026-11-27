"""
Módulo: formularios.py
Responsable: Integrante 5
Función: Controles de entrada en la barra lateral (Sidebar) de Streamlit.
"""

import streamlit as st
from typing import Dict, Any


def renderizar_sidebar_inputs() -> Dict[str, Any]:
    """Construye el formulario lateral con valores precargados del escenario base (60 km)."""
    st.sidebar.header("Parámetros del Enlace Óptico")
    tipo_fibra = st.sidebar.selectbox(
        "Estándar de Fibra Óptica",
        [
            "UIT-T G.652.D (Monomodo Estándar)",
            "UIT-T G.655 (Monomodo NZDSF)",
            "ISO/IEC 11801 OS2 (Planta Externa)",
            "ISO/IEC 11801 OM3 (Multimodo 50/125 µm)",
            "ISO/IEC 11801 OM4 (Multimodo 50/125 µm)"
        ]
    )
    longitud_km = st.sidebar.number_input("Longitud del enlace L (km)", min_value=0.1, value=60.0, step=1.0)
    longitud_onda_nm = st.sidebar.selectbox("Longitud de onda λ (nm)", [850, 1300, 1310, 1550], index=3)
    atenuacion_db_km = st.sidebar.number_input("Coeficiente de atenuación α (dB/km)", min_value=0.0, value=0.25, step=0.01)
    p_tx_dbm = st.sidebar.number_input("Potencia del transmisor Ptx (dBm)", min_value=-50.0, max_value=30.0, value=0.0, step=0.5)
    s_rx_dbm = st.sidebar.number_input("Sensibilidad del receptor Srx (dBm)", min_value=-60.0, max_value=0.0, value=-20.0, step=0.5)
    p_sat_dbm = st.sidebar.number_input("Nivel de saturación Psat (dBm)", min_value=-30.0, max_value=20.0, value=0.0, step=0.5)

    st.sidebar.subheader("Eventos Pasivos (TIA-568.3-D)")
    n_conectores = st.sidebar.number_input("Cantidad de conectores (Nc)", min_value=2, value=2, step=1)
    perdida_conector_db = st.sidebar.number_input("Pérdida por conector (dB)", min_value=0.0, value=1.50, step=0.05)
    n_empalmes_fusion = st.sidebar.number_input("Empalmes por fusión (Nf)", min_value=0, value=0, step=1)
    perdida_fusion_db = st.sidebar.number_input("Pérdida por fusión (dB)", min_value=0.0, value=0.05, step=0.01)

    return {
        "tipo_fibra": tipo_fibra,
        "longitud_km": longitud_km,
        "longitud_onda_nm": longitud_onda_nm,
        "atenuacion_db_km": atenuacion_db_km,
        "p_tx_dbm": p_tx_dbm,
        "s_rx_dbm": s_rx_dbm,
        "p_sat_dbm": p_sat_dbm,
        "n_conectores": n_conectores,
        "perdida_conector_db": perdida_conector_db,
        "n_empalmes_fusion": n_empalmes_fusion,
        "perdida_fusion_db": perdida_fusion_db
    }