"""
Pruebas unitarias para el módulo controlador/validaciones.py (RF-01 / RNF-03)
"""

from controlador.validaciones import ParametrosEnlace


def test_parametros_validos_caso_base():
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


def test_rechazo_longitud_negativa():
    params = ParametrosEnlace(
        longitud_km=-5.0,
        longitud_onda_nm=1550,
        tipo_fibra="G.652.D",
        atenuacion_db_km=0.25,
        p_tx_dbm=0.0,
        s_rx_dbm=-20.0
    )
    valido, mensaje = params.validar()
    assert valido is False
    assert "longitud" in mensaje.lower()


def test_rechazo_longitud_onda_fuera_rango():
    params = ParametrosEnlace(
        longitud_km=10.0,
        longitud_onda_nm=500,
        tipo_fibra="G.652.D",
        atenuacion_db_km=0.25,
        p_tx_dbm=0.0,
        s_rx_dbm=-20.0
    )
    valido, _ = params.validar()
    assert valido is False