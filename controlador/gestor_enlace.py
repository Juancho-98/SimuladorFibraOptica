"""
Módulo Controlador Principal: gestor_enlace.py
Proyecto 1: Simulador para diseño y establecimiento de enlaces de fibra óptica
Equipo 3 - Redes de Telecomunicaciones
Responsable: Scarlett(Orquestación y Reportes)
"""

from dataclasses import asdict
from typing import Dict, Any
import json
import csv
import io

from controlador.validaciones import ParametrosEnlace
from controlador.desiciones import evaluar_viabilidad


def exportar_json(parametros: ParametrosEnlace, resultados: Dict[str, Any]) -> str:
    """Genera salida estructurada en formato JSON (RF-09)."""
    payload = {
        "parametros_entrada": asdict(parametros),
        "resultados_simulacion": resultados
    }
    return json.dumps(payload, indent=4, ensure_ascii=False)


def exportar_csv(parametros: ParametrosEnlace, resultados: Dict[str, Any]) -> str:
    """Genera salida tabular en formato CSV (RF-09)."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Categoria", "Parametro", "Valor"])
    for k, v in asdict(parametros).items():
        writer.writerow(["Entrada", k, v])
    for k, v in resultados.items():
        writer.writerow(["Resultado", k, v])
    return output.getvalue()


if __name__ == "__main__":
    # Verificación rápida del flujo integrado del controlador (Caso base 60 km)
    caso_base = ParametrosEnlace(
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
    es_valido, mensaje = caso_base.validar()
    print("Validación:", es_valido, "-", mensaje)
    veredicto = evaluar_viabilidad(p_rx_dbm=-18.0, s_rx_dbm=-20.0, p_sat_dbm=0.0, margen_diseno_db=3.0)
    print("Veredicto Caso Base:", veredicto)