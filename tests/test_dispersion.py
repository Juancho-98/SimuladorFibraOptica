"""
Pruebas unitarias para el módulo modelo/dispersion.py
"""

from modelo.dispersion import calcular_dispersion_y_capacidad


def test_dispersion_monomodo_60km():
    res = calcular_dispersion_y_capacidad(
        longitud_km=60.0,
        dispersion_cromatica_ps_nm_km=18.0,
        anchura_espectral_nm=0.1,
        bw_modal_mhz_km=None,
        tasa_bits_gbps=10.0,
        snr_db=20.0
    )
    assert res["dt_cromatica_ps"] == 108.0
    assert res["dt_modal_ps"] == 0.0
    assert res["dt_total_ps"] == 108.0
    assert res["capacidad_shannon_gbps"] > 0


def test_dispersion_multimodo_om3():
    res = calcular_dispersion_y_capacidad(
        longitud_km=2.0,
        dispersion_cromatica_ps_nm_km=85.0,
        anchura_espectral_nm=1.0,
        bw_modal_mhz_km=2000.0,
        tasa_bits_gbps=10.0,
        snr_db=20.0
    )
    assert res["dt_modal_ps"] > 0
    assert res["dt_total_ps"] > res["dt_cromatica_ps"]