"""
Integration testing with the Image API (Lab 1)
"""

import io
import pytest
from fastapi.testclient import TestClient
from PIL import Image
from api.api import app


@pytest.fixture
def client():
    """Testing client from FastAPI."""
    return TestClient(app)


def get_test_image_bytes():
    """Función auxiliar para crear una imagen dummy en memoria (bytes)."""
    img = Image.new("RGB", (100, 100), color="blue")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)
    return img_byte_arr


def test_home_endpoint(client):
    """Verify that the endpoint / returns the HTML page."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_predict_endpoint(client):
    """Verify that the endpoint /predict processes an image correctly."""
    img_bytes = get_test_image_bytes()

    # Enviamos el archivo como 'file' (Multipart)
    response = client.post(
        "/predict", files={"file": ("test.jpg", img_bytes, "image/jpeg")}
    )

    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "filename" in data


def test_resize_endpoint(client):
    """Verify that the endpoint /resize resizes the image correctly."""
    img_bytes = get_test_image_bytes()

    # Enviamos archivo + datos de formulario (width, height)
    response = client.post(
        "/resize",
        files={"file": ("test.jpg", img_bytes, "image/jpeg")},
        data={"width": 50, "height": 50},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Image resized successfully"
    assert data["new_size"] == [50, 50]
