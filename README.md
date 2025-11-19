# MLOps Lab 1: Image Processing API & CLI

![CI Status](AQUÍ_PEGA_TU_BADGE_DE_GITHUB)

Este repositorio contiene la solución para el Laboratorio 1 de la asignatura MLOps. El proyecto consiste en una herramienta Python para procesar imágenes (predicción de clase, redimensionado, escala de grises) accesible mediante **CLI** (Línea de Comandos) y **API REST** (FastAPI).

## 🚀 Funcionalidades

* **Predict:** Predice la clase de una imagen (mock).
* **Resize:** Redimensiona una imagen a un ancho y alto específicos.
* **Grayscale:** Convierte una imagen a blanco y negro.
* **Flatten:** Aplana la matriz de la imagen a una lista de píxeles.

## 🛠️ Requisitos e Instalación

Este proyecto utiliza **uv** para la gestión de dependencias.

```bash
# 1. Clonar el repositorio
git clone <TU_URL_DEL_REPO>
cd MLOps-Lab1

# 2. Instalar dependencias
make install
# O manualmente: uv sync
