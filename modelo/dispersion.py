"""
Módulo: dispersion.py
Responsable: Integrante 3
Función: Catálogo normativo de fibras, cálculo de dispersión, límite ISI y capacidad de canal (RF-07).
"""

import numpy as np
from typing import Dict, Any

CATALOGO_FIBRAS: Dict[str, Dict[str, Any]] = {
    "UIT-T G.652.D (Monomodo Estándar)": {
        "tipo": "SMF",
        "atenuacion_1310": 0.35,
        "atenuacion_1550": 0.20,
        "dispersion_cromatica_ps_nm_km": 18.0,
        "bw_modal_mhz_km": None
    },
    "UIT-T G.655 (Monomodo NZDSF)": {
        "tipo": "SMF",
        "atenuacion_1310": 0.35,
        "atenuacion_1550": 0.20,
        "dispersion_cromatica_ps_nm_km": 4.5,
        "bw_modal_mhz_km": None
    },
    "ISO/IEC 11801 OS2 (Planta Externa)": {
        "tipo": "SMF",
        "atenuacion_1310": 0.40,
        "atenuacion_1550": 0.40,
        "dispersion_cromatica_ps_nm_km": 18.0,
        "bw_modal_mhz_km": None
    },
    "ISO/IEC 11801 OM3 (Multimodo 50/125 µm)": {
        "tipo": "MMF",
        "atenuacion_850": 3.0,
        "atenuacion_1300": 1.5,
        "dispersion_cromatica_ps_nm_km": 85.0,
        "bw_modal_mhz_km": 2000.0
    },
    "ISO/IEC 11801 OM4 (Multimodo 50/125 µm)": {
        "tipo": "MMF",
        "atenuacion_850": 3.0,
        "atenuacion_1300": 1.5,
        "dispersion_cromatica_ps_nm_km": 85.0,
        "bw_modal_mhz_km": 4700.0
    }
}


def calcular_dispersion_y_capacidad(
    longitud_km: float,
    dispersion_cromatica_ps_nm_km: float = 18.0,
    anchura_espectral_nm: float = 0.1,
    bw_modal_mhz_km: float = None,
    tasa_bits_gbps: float = 10.0,
    snr_db: float = 20.0,
    niveles_nyquist: int = 2
) -> Dict[str, Any]:
    """Calcula ensanchamiento temporal, ancho de banda efectivo, ISI, Nyquist y Shannon-Hartley (RF-07)."""
    # 1. Dispersión cromática (ps)
    dt_crom_ps = abs(dispersion_cromatica_ps_nm_km) * anchura_espectral_nm * longitud_km

    # 2. Dispersión modal (ps) si es multimodo
    if bw_modal_mhz_km and bw_modal_mhz_km > 0:
        bw_efectivo_modal_ghz = (bw_modal_mhz_km / longitud_km) / 1000.0
        dt_mod_ps = (0.44 / bw_efectivo_modal_ghz) * 1000.0
    else:
        dt_mod_ps = 0.0

    # 3. Ensanchamiento total RMS (ps)
    dt_total_ps = float(np.sqrt(dt_crom_ps**2 + dt_mod_ps**2))

    # 4. Ancho de banda óptico efectivo a -3 dB (GHz)
    if dt_total_ps > 0:
        bw_eff_ghz = 350.0 / dt_total_ps  # 0.35 / dt_s en GHz
        tasa_max_isi_gbps = 700.0 / dt_total_ps  # Criterio NRZ: dt <= 0.7 * Tb
    else:
        bw_eff_ghz = 100.0
        tasa_max_isi_gbps = 100.0

    # 5. Capacidad teórica de Nyquist y Shannon-Hartley (Gbps)
    cap_nyquist_gbps = 2.0 * bw_eff_ghz * np.log2(max(2, niveles_nyquist))
    snr_lineal = 10 ** (snr_db / 10.0)
    cap_shannon_gbps = bw_eff_ghz * np.log2(1.0 + snr_lineal)

    cumple_isi = tasa_bits_gbps <= tasa_max_isi_gbps

    return {
        "dt_cromatica_ps": round(dt_crom_ps, 3),
        "dt_modal_ps": round(dt_mod_ps, 3),
        "dt_total_ps": round(dt_total_ps, 3),
        "ancho_banda_eff_ghz": round(float(bw_eff_ghz), 3),
        "tasa_max_libre_isi_gbps": round(float(tasa_max_isi_gbps), 3),
        "cumple_criterio_isi": bool(cumple_isi),
        "capacidad_nyquist_gbps": round(float(cap_nyquist_gbps), 3),
        "capacidad_shannon_gbps": round(float(cap_shannon_gbps), 3)
    }