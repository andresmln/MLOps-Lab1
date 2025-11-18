"""
Aquí es donde hacemos el resize, etc y ademas tenemos que merte 
"""

import random
from PIL import Image

def predict(image: Image.Image) -> str:
    """
    Predecir la clase de una imagen dada aleatoriamente.
    """
    # Definimos un set de clases de ejemplo
    classes = ["gato", "perro", "coche", "avión"]
    return random.choice(classes)

def resize(image: Image.Image, width: int, height: int) -> Image.Image:
    """
    Redimensionar una imagen a un ancho y alto específicos.
    """
    return image.resize((width, height))
