"""
Aplicación Principal: app.py
Simulador para Diseño y Establecimiento de Enlaces de Fibra Óptica - Equipo 3
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from controlador.validaciones import ParametrosEnlace
from controlador.desiciones import evaluar_viabilidad
from modelo.potencia import calcular_balance_potencia, generar_perfil_espacial
from modelo.dispersion import calcular_dispersion_y_capacidad
from vista.formularios import renderizar_sidebar_inputs
from vista.dashboard import renderizar_tarjetas_kpi
from vista.graficas import crear_grafica_perfil_potencia

st.set_page_config(page_title="Simulador de Fibra Óptica - Equipo 3", layout="wide")
st.title("Simulador de Enlaces de Telecomunicaciones por Fibra Óptica")
st.caption("Proyecto 1 — Redes de Telecomunicaciones (Equipo 3)")

datos = renderizar_sidebar_inputs()

params = ParametrosEnlace(
    longitud_km=datos["longitud_km"],
    longitud_onda_nm=datos["longitud_onda_nm"],
    tipo_fibra=datos["tipo_fibra"],
    atenuacion_db_km=datos["atenuacion_db_km"],
    p_tx_dbm=datos["p_tx_dbm"],
    s_rx_dbm=datos["s_rx_dbm"],
    p_sat_dbm=datos["p_sat_dbm"],
    n_conectores=datos["n_conectores"],
    perdida_conector_db=datos["perdida_conector_db"],
    n_empalmes_fusion=datos["n_empalmes_fusion"],
    perdida_fusion_db=datos["perdida_fusion_db"]
)

es_valido, mensaje = params.validar()

if not es_valido:
    st.error(mensaje)
else:
    res_pot = calcular_balance_potencia(
        longitud_km=params.longitud_km,
        atenuacion_db_km=params.atenuacion_db_km,
        p_tx_dbm=params.p_tx_dbm,
        s_rx_dbm=params.s_rx_dbm,
        n_empalmes_fusion=params.n_empalmes_fusion,
        perdida_fusion_db=params.perdida_fusion_db,
        n_conectores=params.n_conectores,
        perdida_conector_db=params.perdida_conector_db
    )
    veredicto = evaluar_viabilidad(
        p_rx_dbm=res_pot["p_rx_dbm"],
        s_rx_dbm=params.s_rx_dbm,
        p_sat_dbm=params.p_sat_dbm,
        margen_diseno_db=params.margen_diseno_db
    )
    res_disp = calcular_dispersion_y_capacidad(longitud_km=params.longitud_km)

    renderizar_tarjetas_kpi(res_pot, veredicto)
    st.info(f"**Diagnóstico:** {veredicto['diagnostico']} | **Sugerencia:** {veredicto['recomendacion']}")

    z, pz = generar_perfil_espacial(
        longitud_km=params.longitud_km,
        atenuacion_db_km=params.atenuacion_db_km,
        p_tx_dbm=params.p_tx_dbm,
        perdida_conector_db=params.perdida_conector_db,
        n_conectores=params.n_conectores,
        perdida_empalmes_total_db=params.n_empalmes_fusion * params.perdida_fusion_db
    )
    fig = crear_grafica_perfil_potencia(z, pz, params.s_rx_dbm, params.p_sat_dbm)
    st.plotly_chart(fig, use_container_width=True)