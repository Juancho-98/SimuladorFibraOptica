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
# Simulador para Diseño y Establecimiento de Enlaces de Fibra Óptica

Herramienta interactiva desarrollada en Python bajo el patrón arquitectónico **Modelo-Vista-Controlador (MVC)** para el cálculo de presupuesto de potencia óptica, ensanchamiento por dispersión, capacidad teórica del canal y diagnóstico normativo de viabilidad basado en recomendaciones **UIT-T G.652.D / G.655**, **ISO/IEC 11801** y **TIA-568.3-D**.

---

## 1. Estructura del Proyecto (Arquitectura MVC)

```text
SimuladorFibraOptica/
├── requirements.txt            # Dependencias del entorno virtual
├── README.md                   # Documentación técnica y guía de ejecución
├── controlador/                # Capa de validación, reglas de negocio y reportes
│   ├── __init__.py
│   ├── validaciones.py         # Restricciones físicas y dimensionales (RF-01 / RNF-03)
│   ├── desiciones.py           # Árbol de decisión técnico de 4 estados (RF-06)
│   └── gestor_enlace.py        # Orquestación y serialización JSON/CSV (RF-09)
├── modelo/                     # Capa matemática y física óptica
│   ├── __init__.py
│   ├── potencia.py             # Atenuación, eventos y balance de potencia (RF-02 a RF-05)
│   └── dispersion.py           # Catálogo normativo, dispersión, ISI y Shannon/Nyquist (RF-07)
├── vista/                      # Capa de interfaz gráfica y visualización
│   ├── __init__.py
│   ├── app.py                  # Punto de entrada principal de la aplicación Streamlit
│   ├── formularios.py          # Controles de entrada en barra lateral
│   ├── dashboard.py            # Tarjetas de métricas KPI y diagnósticos
│   └── graficas.py             # Perfil espacial de potencia en Plotly (RF-08)
└── tests/                      # Aseguramiento de calidad (RNF-01)
    └── test_validaciones.py    # Suite de pruebas unitarias automatizadas con pytest
```

---

## 2. Guía Rápida de Instalación y Pruebas para el Equipo

Para clonar, configurar el entorno y ejecutar las pruebas en cualquier computadora (Windows / PowerShell), sigan estos pasos desde la carpeta raíz `SimuladorFibraOptica`:

### Paso 1: Sincronizar cambios del repositorio
```powershell
git pull origin main
```
*(Si están trabajando en su propia rama, asegúrense de traer los últimos cambios antes de ejecutar).*

### Paso 2: Crear y activar el entorno virtual (`.venv`)
Si aún no tienen creado su entorno virtual local:
```powershell
python -m venv .venv
```
Para activarlo en PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```
*(Si PowerShell bloquea la ejecución de scripts, ejecuten primero: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` y vuelvan a activar).*

### Paso 3: Instalar dependencias
```powershell
pip install -r requirements.txt
```

### Paso 4: Ejecutar pruebas unitarias (`pytest`)
Para verificar que los cálculos matemáticos y las validaciones cumplen con el escenario base ($L = 60\text{ km}$, $A_{total} = 18.0\text{ dB}$, $P_{rx} = -18.0\text{ dBm}$, $M = +2.0\text{ dB}$):
```powershell
python -m pytest -v
```
**Resultado esperado:** `3 passed` en verde.

### Paso 5: Ejecutar la aplicación web (`Streamlit`)
Para abrir el simulador en el navegador:
```powershell
python -m streamlit run vista/app.py
```
*(La primera vez que se ejecute Streamlit, pedirá un correo en consola; solo presionen **Enter** dejándolo en blanco).*

---

## 3. Estado Actual de Avance (Cierre de Semana 4)

* [x] **Especificación y Modelado Matemático (Semanas 1–3):** Definición de requerimientos (SRS), demostración analítica del caso base de $60\text{ km}$ y diseño de arquitectura MVC.
* [x] **Capa Controladora (`controlador/`):** Implementación de `ParametrosEnlace` con validación estricta de rangos físicos (`RF-01`), clasificación de viabilidad en 4 estados (`RF-06`) y exportación base a JSON/CSV (`RF-09`).
* [x] **Capa de Modelo (`modelo/`):** Implementación de funciones vectorizadas para balance de potencia, pérdidas por empalmes/conectores, perfil espacial $P(z)$, catálogo de fibras normativas, ensanchamiento por dispersión, criterio libre de ISI y límites de Nyquist / Shannon-Hartley.
* [x] **Capa de Vista Base (`vista/`):** Estructura funcional en Streamlit con barra lateral de parámetros, tarjetas KPI y gráfica interactiva de perfil de potencia en Plotly.
* [x] **Pruebas Unitarias (`tests/`):** Validación automatizada con `pytest` aprobada al 100% sin desviación respecto al cálculo manual.

---

## 4. Hoja de Ruta — Pendientes para Próximas Semanas

### Semana 5: Refinamiento Visual y Reportes Técnicos
* **Integrante 4 (Controlador/Reportes):** Implementar la generación y descarga directa del **reporte técnico en PDF** (`fpdf2`) incrustando la gráfica de Plotly (`kaleido`) y la tabla de resultados (`RF-09`), además de habilitar los botones de descarga CSV y JSON en la interfaz.
* **Integrante 5 (UI/Formularios):** Conectar la selección del estándar de fibra (`UIT-T G.652.D`, `G.655`, `OM3`, `OM4`) para que autorrellene automáticamente los valores sugeridos de atenuación ($\alpha$) y dispersión en el formulario.

### Semana 6: Integración Completa de Dispersión y Alcance Máximo
* **Integrante 3 y 5:** Agregar la sección de resultados de **Dispersión y Capacidad del Canal** en el panel principal de `dashboard.py` (mostrando $\Delta T_{total}$, ancho de banda efectivo $B_{eff}$, cumplimiento de ISI, Nyquist y Shannon-Hartley).
* **Integrante 6 (Gráficas):** Incorporar la segunda gráfica interactiva en `graficas.py` comparando el **alcance máximo limitado por atenuación vs. limitado por dispersión**.

### Semanas 7 y 8: Pruebas de Estrés, Validación Final y Entrega
* **Integrante 1 y Todo el Equipo:** Ejecutar pruebas de frontera con enlaces multimodo de alta velocidad, enlaces saturados ($P_{rx} > P_{sat}$) y enlaces de larga distancia con atenuación crítica; actualizar documentación final y preparar la demostración de cierre.