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
