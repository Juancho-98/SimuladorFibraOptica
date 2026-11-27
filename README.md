# Simulador de Enlaces de Fibra Óptica

Proyecto de Redes de Telecomunicaciones basado en la arquitectura Modelo - Vista - Controlador (MVC).

## Repositorio Oficial

https://github.com/Juancho-98/SimuladorFibraOptica

---

# Stack Tecnológico

- Python 3.12.10
- NumPy
- SciPy
- Pandas
- Streamlit
- Plotly
- Pytest

---

# Instalación de Python

## Verificar versión instalada

Abrir PowerShell:

```powershell
python --version
```

Debe mostrar:

```text
Python 3.12.10
```

---

# Clonar el Proyecto

```powershell
git clone https://github.com/Juancho-98/SimuladorFibraOptica.git
```

Entrar al proyecto:

```powershell
cd SimuladorFibraOptica
```

---

# Crear Entorno Virtual

Desde la carpeta del proyecto:

```powershell
python -m venv .venv
```

Activar entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

La terminal debe cambiar a:

```text
(.venv) PS ...
```

---

# Instalación de Dependencias

Instalar todas las librerías necesarias:

```powershell
pip install numpy scipy pandas plotly streamlit pytest
```

Verificar instalación:

```powershell
pip list
```

---

# Actualizar requirements.txt

Cuando se agreguen o actualicen librerías:

```powershell
pip freeze > requirements.txt
```

Instalar dependencias desde requirements.txt:

```powershell
pip install -r requirements.txt
```

---

# Uso de Git

## Clonar repositorio

```powershell
git clone https://github.com/Juancho-98/SimuladorFibraOptica.git
```

## Crear rama personal

Ejemplo:

```powershell
git checkout -b integrante2-potencia
```

Subir rama:

```powershell
git push -u origin integrante2-potencia
```

---

# Flujo de Trabajo

Antes de comenzar cada sesión:

```powershell
git pull
```

Agregar cambios:

```powershell
git add .
```

Crear commit:

```powershell
git commit -m "Descripción del cambio"
```

Subir cambios:

```powershell
git push
```

---

# IMPORTANTE

NO trabajar directamente sobre:

```text
main
```

Cada integrante trabajará únicamente en su rama personal.

---

# Estructura del Proyecto

```text
SimuladorFibraOptica
│
├── modelo
├── controlador
├── vista
├── tests
├── docs
├── data
├── assets
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

# Distribución de Responsabilidades

## Integrante 1

Arquitectura MVC, Git y QA

Responsable de:

- Configuración del repositorio
- Integración de ramas
- Pruebas unitarias
- Validación de entregables

---

## Integrante 2

Modelado Físico - Potencia

Archivos:

```text
modelo/potencia.py
tests/test_potencia.py
```

Responsable de:

- Atenuación
- Pérdidas
- Potencia recibida
- Margen
- Viabilidad

---

## Integrante 3

Modelado Físico - Dispersión

Archivos:

```text
modelo/dispersion.py
tests/test_dispersion.py
```

Responsable de:

- Dispersión cromática
- Dispersión modal
- ISI
- Nyquist
- Shannon

---

## Integrante 4

Controlador

Archivos:

```text
controlador/gestor_enlace.py
controlador/validaciones.py
controlador/decisiones.py
```

Responsable de:

- Validación de entradas
- Orquestación MVC
- Comunicación Vista ↔ Modelo

---

## Integrante 5

Frontend Streamlit

Archivos:

```text
vista/app.py
vista/formularios.py
vista/dashboard.py
```

Responsable de:

- Formularios
- KPIs
- Interfaz de usuario

---

## Integrante 6

Visualización Científica

Archivos:

```text
vista/graficas.py
```

Responsable de:

- Gráficas Plotly
- Curvas de potencia
- Curvas de capacidad

---

# Archivos Ignorados por Git

Archivo:

```text
.gitignore
```

Contenido:

```gitignore
__pycache__/
*.pyc

.venv/
venv/

.vscode/

.pytest_cache/

*.log

Thumbs.db
Desktop.ini
```
----------------------------------------------------------------------------------------
## Simulador para Diseño y Establecimiento de Enlaces de Fibra Óptica

**Materia:** Redes de Telecomunicaciones  
**Proyecto:** Proyecto 1  
**Equipo:** Equipo 3  

Herramienta interactiva desarrollada en Python bajo el patrón arquitectónico **Modelo-Vista-Controlador (MVC)** para el cálculo de presupuesto de potencia óptica, ensanchamiento por dispersión, capacidad teórica del canal y diagnóstico normativo de viabilidad basado en recomendaciones **UIT-T G.652.D / G.655**, **ISO/IEC 11801** y **TIA-568.3-D**.

---

## 1. ¿Cómo funciona el sistema? (Flujo Arquitectónico MVC)

El proyecto separa la lógica matemática de la interfaz gráfica para que cada módulo pueda probarse de forma independiente:

1. **Entrada y Validación (`controlador/validaciones.py`):** Recibe los parámetros físicos del enlace ($L$, $\lambda$, $P_{tx}$, $S_{rx}$, $P_{sat}$, conectores y empalmes) y verifica que cumplan restricciones físicas reales ($L > 0$, $\lambda \in [800, 1650]\text{ nm}$, $S_{rx} < P_{sat}$, $N_c \ge 2$) antes de permitir cualquier cálculo.
2. **Motor Matemático (`modelo/`):**
   * `enlace.py` y `resultados.py` definen las estructuras de datos del medio físico y de salida.
   * `potencia.py` calcula la atenuación lineal ($\alpha \cdot L$), pérdidas concentradas por eventos pasivos, potencia recibida ($P_{rx}$ en dBm y mW/$\mu$W), margen de seguridad ($M$) y el vector espacial $P(z)$ a lo largo de la fibra.
   * `dispersion.py` consulta el catálogo normativo y calcula el ensanchamiento cromático/modal ($\Delta t_{total}$), el ancho de banda efectivo a $-3\text{ dB}$, la tasa máxima libre de ISI y la capacidad teórica de Nyquist y Shannon-Hartley.
3. **Evaluación de Viabilidad (`controlador/desiciones.py`):** Clasifica el enlace en 4 estados operativos (*Viable y óptimo*, *Crítico / En riesgo*, *No viable por atenuación* o *No viable por saturación*) y emite recomendaciones técnicas.
4. **Interfaz y Gráficas (`vista/`):** `formularios.py` captura los datos en la barra lateral, `dashboard.py` despliega los indicadores clave (KPI) y `graficas.py` renderiza las curvas interactivas en Plotly.

---

## 2. Estructura del Proyecto

```text
SimuladorFibraOptica/
├── requirements.txt            # Dependencias del entorno virtual
├── README.md                   # Documentación técnica y guía de ejecución
├── modelo/                     # Capa matemática y física óptica (Semana 4)
│   ├── __init__.py
│   ├── enlace.py               # Entidad de dominio del enlace físico y componentes pasivos
│   ├── potencia.py             # Atenuación, eventos y balance de potencia (RF-02 a RF-05)
│   ├── dispersion.py           # Catálogo normativo, dispersión, ISI y Shannon/Nyquist (RF-07)
│   └── resultados.py           # Estructura estandarizada de resultados numéricos
├── vista/                      # Capa de interfaz gráfica y visualización (Semana 5)
│   ├── __init__.py
│   ├── app.py                  # Punto de entrada principal de la aplicación Streamlit
│   ├── formularios.py          # Controles de entrada en barra lateral
│   ├── dashboard.py            # Tarjetas de métricas KPI y diagnósticos
│   └── graficas.py             # Perfil espacial de potencia en Plotly (RF-08)
├── controlador/                # Capa de validación, reglas de negocio y enlace MVC (Semana 6)
│   ├── __init__.py
│   ├── validaciones.py         # Restricciones físicas y dimensionales (RF-01 / RNF-03)
│   ├── desiciones.py           # Árbol de decisión técnico de 4 estados (RF-06)
│   └── gestor_enlace.py        # Orquestación y serialización JSON/CSV (RF-09)
└── tests/                      # Pruebas unitarias lógicas independientes
    ├── __init__.py
    ├── test_potencia.py        # Pruebas unitarias de balance de potencia
    ├── test_dispersion.py      # Pruebas unitarias de dispersión y capacidad
    ├── test_validaciones.py    # Pruebas unitarias de validación de entradas
    └── test_desiciones.py      # Pruebas unitarias del árbol de decisión
```

---

## 3. Responsabilidades y Avance por Integrante (Etapa 2)

| Integrante | Rol / Módulo Asignado | Archivos en el Repo | Qué ya está hecho (Semana 4) | Qué falta por hacer (Semanas 5 y 6) |
| :--- | :--- | :--- | :--- | :--- |
| **Integrante 1** | **Arquitectura y QA** | `requirements.txt`<br>`tests/*.py` | Estructura base MVC, configuración de `.venv` y suite de 12 pruebas unitarias independientes en `pytest`. | Ampliar pruebas unitarias para casos extremos (fibra multimodo OM3/OM4, saturación) y validar integración final en `main`. |
| **Integrante 2** | **Modelo: Potencia y Enlace** | `modelo/enlace.py`<br>`modelo/potencia.py`<br>`modelo/resultados.py` | Clases `EnlaceOptico` y `ResultadoSimulacion`, ecuaciones de atenuación, eventos pasivos, balance de potencia y vector espacial $P(z)$. | Verificar precisión numérica frente a nuevos escenarios de prueba y enlazar salida directa con `ResultadoSimulacion`. |
| **Integrante 3** | **Modelo: Dispersión y Catálogo** | `modelo/dispersion.py` | Catálogo normativo (G.652.D, G.655, OS2, OM3, OM4), cálculo de $\Delta t$, ancho de banda efectivo, límite ISI, Nyquist y Shannon. | Conectar la selección automática de parámetros del catálogo con los controles de la interfaz y calcular alcance máximo por dispersión. |
| **Integrante 4** | **Controlador, Validación y Reportes** | `controlador/validaciones.py`<br>`controlador/desiciones.py`<br>`controlador/gestor_enlace.py` | Clase `ParametrosEnlace` con validación estricta (`RF-01`), árbol de decisión de 4 estados (`RF-06`) y exportación base JSON/CSV. | Implementar la función orquestadora completa en `gestor_enlace.py` y agregar la generación del reporte técnico descargable en PDF (`fpdf2`). |
| **Integrante 5** | **Vista: UI y Formularios** | `vista/app.py`<br>`vista/formularios.py`<br>`vista/dashboard.py` | Esqueleto funcional en Streamlit con barra lateral de parámetros, tarjetas KPI y despliegue de diagnóstico técnico. | Refinar diseño visual, mostrar en el dashboard los resultados de dispersión/capacidad y añadir botones de descarga (PDF/JSON/CSV). |
| **Integrante 6** | **Vista: Gráficas Interactivas** | `vista/graficas.py` | Gráfica interactiva en Plotly del perfil espacial de potencia $P(z)$ con líneas límite de sensibilidad ($S_{rx}$) y saturación ($P_{sat}$). | Añadir la segunda gráfica comparativa de alcance máximo (atenuación vs. dispersión) y exportación de imagen estática (`kaleido`) para el PDF. |

---

## 4. Guía Rápida de Instalación y Pruebas para el Equipo

Desde la carpeta raíz `SimuladorFibraOptica` en VS Code (PowerShell), sigan estos pasos:

### Paso 1: Sincronizar cambios del repositorio
```powershell
git pull origin main
```

### Paso 2: Crear y activar el entorno virtual (`.venv`)
Si aún no tienen su entorno virtual local:
```powershell
python -m venv .venv
```
Para activarlo en PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```
*(Si PowerShell bloquea los scripts, ejecuten primero: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` y vuelvan a activar).*

### Paso 3: Instalar dependencias
```powershell
pip install -r requirements.txt
```

### Paso 4: Ejecutar pruebas unitarias lógicas independientes (`pytest`)
Para verificar de forma aislada los algoritmos matemáticos del Modelo y sus reglas lógicas (incluyendo el caso base $L = 60\text{ km}$, $A_{total} = 18.0\text{ dB}$, $P_{rx} = -18.0\text{ dBm}$, $M = +2.0\text{ dB}$):
```powershell
python -m pytest -v
```
**Resultado esperado:** `12 passed` en verde.

### Paso 5: Ejecutar la vista en navegador (`Streamlit`)
```powershell
python -m streamlit run vista/app.py
```
*(La primera vez pedirá un correo en consola; presionen **Enter** dejándolo en blanco).*

---

## 5. Cronograma Oficial — Etapa 2: Diseño del Sistema (Semanas 4 a 6)

* [x] **Semana 4: Diseño del Módulo de Modelo (Lógica de Negocio)**
  * *Actividades:* Estructuración de las clases, funciones y librerías científicas (`NumPy`/`SciPy`) encargadas de ejecutar los algoritmos matemáticos del simulador de fibra (`enlace.py`, `potencia.py`, `dispersion.py` y `resultados.py`).
  * *Entregable:* Código base estructurado para el Modelo con pruebas unitarias lógicas independientes (`tests/` ejecutadas mediante `pytest`).
* [ ] **Semana 5: Diseño de la Interfaz (Vista)**
  * *Actividades:* Construcción y refinamiento de los componentes visuales de la interfaz de usuario en `vista/` (formularios de entrada de parámetros como longitud, potencia de transmisión, selección automática de fibra y gráficos interactivos de resultados).
  * *Entregable:* Interfaz visual estática e interactiva integrada con el diseño propuesto.
* [ ] **Semana 6: Diseño de Controladores y Enlace de Componentes**
  * *Actividades:* Desarrollo e integración completa de la capa controladora (`controlador/`) que intermedia entre las acciones del usuario en la Vista y los cálculos procesados por el Modelo, incluyendo exportación de reportes y pruebas de flujo de datos iniciales.
  * *Entregable:* Primera versión integrada del patrón MVC comunicando datos de prueba básicos de extremo a extremo.