"""
Suite de Pruebas Unitarias: test_validacion.py
Responsable: Integrante 1 (QA)
Ejecución: pytest -v
"""

from controlador.validaciones import ParametrosEnlace
from controlador.desiciones import evaluar_viabilidad
from modelo.potencia import calcular_balance_potencia
from modelo.dispersion import calcular_dispersion_y_capacidad


def test_escenario_base_60km():
    """Valida el criterio de aceptación oficial: L=60km, Ptx=0dBm, alpha=0.25, Lconn=3dB, Srx=-20dBm."""
    params = ParametrosEnlace(
        longitud_km=60.0,
        longitud_onda_nm=1550,
        tipo_fibra="UIT-T G.652.D",
        atenuacion_db_km=0.25,
        p_tx_dbm=0.0,
        s_rx_dbm=-20.0,
        p_sat_dbm=0.0,
        n_conectores=2,
        perdida_conector_db=1.5
    )
    valido, _ = params.validar()
    assert valido is True

    res = calcular_balance_potencia(
        longitud_km=params.longitud_km,
        atenuacion_db_km=params.atenuacion_db_km,
        p_tx_dbm=params.p_tx_dbm,
        s_rx_dbm=params.s_rx_dbm,
        n_conectores=params.n_conectores,
        perdida_conector_db=params.perdida_conector_db
    )
    assert res["perdida_total_db"] == 18.0
    assert res["p_rx_dbm"] == -18.0
    assert res["margen_seguridad_db"] == 2.0

    veredicto = evaluar_viabilidad(res["p_rx_dbm"], params.s_rx_dbm, params.p_sat_dbm)
    assert veredicto["viable"] is True
    assert veredicto["estado"] == "CRÍTICO / EN RIESGO"


def test_rechazo_longitud_invalida():
    """Verifica que RNF-03 bloquee distancias nulas o negativas."""
    params = ParametrosEnlace(
        longitud_km=-5.0,
        longitud_onda_nm=1550,
        tipo_fibra="G.652.D",
        atenuacion_db_km=0.25,
        p_tx_dbm=0.0,
        s_rx_dbm=-20.0
    )
    valido, _ = params.validar()
    assert valido is False


def test_modulo_dispersion():
    """Verifica que el cálculo de dispersión y capacidad retorne valores positivos coherentes."""
    res = calcular_dispersion_y_capacidad(longitud_km=60.0)
    assert res["dt_total_ps"] > 0
    assert res["capacidad_shannon_gbps"] > 0