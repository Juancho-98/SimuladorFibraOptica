"""
Pruebas unitarias para el módulo modelo/potencia.py
"""

from modelo.potencia import (
    calcular_atenuacion_fibra,
    calcular_perdidas_eventos,
    calcular_balance_potencia
)


def test_atenuacion_fibra_60km():
    assert calcular_atenuacion_fibra(longitud_km=60.0, atenuacion_db_km=0.25) == 15.0


def test_perdidas_eventos_conectores():
    perdidas = calcular_perdidas_eventos(
        n_empalmes_fusion=0,
        perdida_fusion_db=0.05,
        n_empalmes_mecanicos=0,
        perdida_mecanica_db=0.30,
        n_conectores=2,
        perdida_conector_db=1.5
    )
    assert perdidas == 3.0


def test_balance_potencia_caso_base():
    res = calcular_balance_potencia(
        longitud_km=60.0,
        atenuacion_db_km=0.25,
        p_tx_dbm=0.0,
        s_rx_dbm=-20.0,
        n_conectores=2,
        perdida_conector_db=1.5
    )
    assert res["perdida_total_db"] == 18.0
    assert res["p_rx_dbm"] == -18.0
    assert res["margen_seguridad_db"] == 2.0