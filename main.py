from fastapi import FastAPI, File, UploadFile
from manga_ocr import MangaOcr
from PIL import Image
from io import BytesIO

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/api/ocr")
async def ocr(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(BytesIO(content))
    ocr = MangaOcr()
    text = ocr(image)

    return {"result": text}
