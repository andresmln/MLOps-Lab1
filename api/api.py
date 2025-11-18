# Import the libraries, classes and functions
import uvicorn
from fastapi import FastAPI, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from mylib.logic import predict, resize 
from PIL import Image
import io

# from pydantic import BaseModel
from mylib.calculator import add, subtract, multiply, divide, power

app = FastAPI(title="MLOps Lab1 API",
            description="API to perform arithmetical operations using mylib.calculator",
            version="1.0.0",)

@app.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    """
    Endpoint para predecir la clase de una imagen subida.
    Recibe un archivo binario (UploadFile).
    """
    # Leer la imagen
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    prediction = predict(image)
    return {"filename": file.filename, "prediction": prediction}

@app.post("/resize")
async def resize_endpoint(
    file: UploadFile = File(...),
    width: int = Form(...),
    height: int = Form(...)
):
    """
    Endpoint para redimensionar una imagen.
    Recibe archivo y parámetros width/height via Form.
    """
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        resized_image = resize(image, width, height)
        
        # Para devolver la imagen, podríamos guardarla en un buffer y devolverla,
        # o simplemente confirmar que se hizo el resize con sus nuevas dimensiones.
        return {
            "original_size": image.size,
            "new_size": resized_image.size,
            "message": "Image resized successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# We use the templates folder to obtain HTML files
templates = Jinja2Templates(directory="templates")


# Initial endpoint
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


# # Input class (with Pydantic) to define the input arguments of the calculator
# class CalcRequest(BaseModel):
#     operation: str
#     a: float
#     b: float


# Main endpoint to perform the artihmetical operations using the input class defined with Pydantic
@app.post("/calculate")
async def calculate(op: str = Form(), a: float = Form(), b: float = Form()):
    """
    It performs an arithmetical operation according to the input parameters.
    """
    op = op.lower()

    if op not in ["add", "subtract", "multiply", "divide", "power"]:
        raise HTTPException(status_code=400, detail="Unvalid operation")

    result = None
    if op == "add":
        result = add(a, b)
    elif op == "subtract":
        result = subtract(a, b)
    elif op == "multiply":
        result = multiply(a, b)
    elif op == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Zero division not allowed")
        result = divide(a, b)
    elif op == "power":
        result = power(a, b)

    return {"result": result}


# # Main endpoint to perform the artihmetical operations using the input class defined with Pydantic
# @app.post("/calculate")
# def calculate(data: CalcRequest):
#     """
#     It performs an arithmetical operation according to the input parameters.
#     """
#     op = data.operation.lower()
#     a = data.a
#     b = data.b

#     if op not in ["add", "subtract", "multiply", "divide", "power"]:
#         raise HTTPException(status_code=400, detail="Unvalid operation")

#     result = None
#     if op == "add":
#         result = add(a, b)
#     elif op == "subtract":
#         result = subtract(a, b)
#     elif op == "multiply":
#         result = multiply(a, b)
#     elif op == "divide":
#         if b == 0:
#             raise HTTPException(status_code=400, detail="Zero division not allowed")
#         result = divide(a, b)
#     elif op == "power":
#         result = power(a, b)

#     return {"result": result}


# Entry point (for direct execution only)
if __name__ == "__main__":
    uvicorn.run("api.api:app", host="0.0.0.0", port=8000, reload=True)
