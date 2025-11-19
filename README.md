# MLOps Lab 1: Image Processing API & CLI

![CI Status](PASTE_YOUR_GITHUB_BADGE_HERE)

This repository contains the solution for Lab 1 of the MLOps course. The project consists of a Python tool for image processing (class prediction, resizing, grayscale conversion, and flattening) accessible via both a **CLI** (Command Line Interface) and a **REST API** (FastAPI).

## 🚀 Features

* **Predict:** Predicts the class of a given image (mock implementation)
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