"""
Pruebas unitarias para el módulo controlador/desiciones.py (RF-06)
"""

from controlador.desiciones import evaluar_viabilidad


def test_estado_viable_y_optimo():
    res = evaluar_viabilidad(p_rx_dbm=-15.0, s_rx_dbm=-20.0, p_sat_dbm=0.0, margen_diseno_db=3.0)
    assert res["viable"] is True
    assert res["estado"] == "VIABLE Y ÓPTIMO"


def test_estado_critico_en_riesgo():
    res = evaluar_viabilidad(p_rx_dbm=-18.0, s_rx_dbm=-20.0, p_sat_dbm=0.0, margen_diseno_db=3.0)
    assert res["viable"] is True
    assert res["estado"] == "CRÍTICO / EN RIESGO"


def test_estado_no_viable_atenuacion():
    res = evaluar_viabilidad(p_rx_dbm=-22.0, s_rx_dbm=-20.0, p_sat_dbm=0.0, margen_diseno_db=3.0)
    assert res["viable"] is False
    assert res["estado"] == "NO VIABLE (Atenuación)"


def test_estado_no_viable_saturacion():
    res = evaluar_viabilidad(p_rx_dbm=2.0, s_rx_dbm=-20.0, p_sat_dbm=0.0, margen_diseno_db=3.0)
    assert res["viable"] is False
    assert res["estado"] == "NO VIABLE (Saturación)"