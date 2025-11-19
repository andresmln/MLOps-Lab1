# MLOps Lab 1: Image Processing API & CLI

[![CI Pipeline](https://github.com/andresmln/MLOps-Lab1/actions/workflows/ci.yml/badge.svg)](https://github.com/andresmln/MLOps-Lab1/actions/workflows/ci.yml)

This repository contains the solution for Lab 1 of the MLOps subject of the UPNA Master's Degree in Machine Learning. The project consists of a Python tool for image processing (class prediction, resizing, grayscale conversion, and flattening) accessible via both a **CLI** (Command Line Interface) and a **REST API** (FastAPI).

## 🚀 Features

* **Predict:** Predicts the class of a given image.
* **Resize:** Resizes an image to specific width and height dimensions.
* **Grayscale:** Converts an image to black and white (preprocessing).
* **Flatten:** Flattens the image matrix into a 1D pixel list.

## 🛠️ Requirements & Installation

This project uses **uv** for dependency management and virtual environments.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <git@github.com:andresmln/MLOps-Lab1.git>
    cd MLOps-Lab1
    ```

2.  **Install dependencies:**
    You can use the Makefile provided:
    ```bash
    make install
    ```
    Or manually using `uv`:
    ```bash
    uv sync
    ```

## 💻 Usage

### 1. Running the API
To start the local server:

```bash
uv run python -m api.api
```
### 2. Using Cli

```bash
# Predict class
uv run python -m cli.cli predict "path/to/image.jpg"

# Resize image (e.g., to 100x100)
uv run python -m cli.cli resize "path/to/image.jpg" 100 100

# Convert to grayscale
uv run python -m cli.cli grayscale "path/to/image.jpg"

# Flatten image
uv run python -m cli.cli flatten "path/to/image.jpg"
```
## 🧪 Development & Quality (Makefile)

According to MLOps best practices, a `Makefile` is included to automate quality checks and testing.

```bash
# Run tests (Pytest)
make test

# Check code quality (Linting + Formatting)
make refactor

# Run everything (Install + Quality + Tests)
make all
```
## 📂 Project Structure
MLOps-Lab1/
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuración del Pipeline de CI (GitHub Actions)
├── api/
│   ├── __init__.py         # (Opcional, pero recomendado)
│   └── api.py              # Código de la API (FastAPI)
├── cli/
│   ├── __init__.py         # (Opcional)
│   └── cli.py              # Código de la Línea de Comandos (Click)
├── mylib/
│   ├── __init__.py         # Marca la carpeta como paquete Python
│   └── logic.py            # Lógica principal (predict, resize, grayscale, flatten)
├── templates/
│   └── home.html           # Página de inicio para la API
├── tests/
│   ├── __init__.py         # (Opcional)
│   ├── test_api.py         # Tests de integración para la API
│   ├── test_cli.py         # Tests para el CLI
│   └── test_logic.py       # Tests unitarios para las funciones de lógica
├── .gitignore              # Archivos a ignorar por Git (.venv, __pycache__, etc.)
├── .python-version         # (Opcional) Versión de Python fijada por uv
├── Makefile                # Automatización de comandos (install, test, lint, all)
├── pyproject.toml          # Configuración del proyecto y dependencias
├── README.md               # Documentación del proyecto
└── uv.lock                 # Archivo de bloqueo de versiones exactas