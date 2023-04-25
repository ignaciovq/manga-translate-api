from fastapi import FastAPI, File, UploadFile, Depends
from PIL import Image
from io import BytesIO
from manga_ocr import MangaOcr
from detection import getBBoxesAndSaveToFile
from imageProcessing import clipTextFromMask, getTextFromClips, get_manga_ocr
from utils import clearFiles

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/api/ocr")
async def ocr(file: UploadFile = File(...), ocr: MangaOcr = Depends(get_manga_ocr)):
    content = await file.read()

    image = Image.open(BytesIO(content))
    image.save(f"assets/imagesToProcess/{file.filename}")
    image.close()

    getBBoxesAndSaveToFile()
    textClips = clipTextFromMask(file.filename)
    text = getTextFromClips(ocr, textClips['clips'])

    response = {"filename": file.filename, "language": textClips['language'], "result": text}

    clearFiles(file.filename, len(textClips['clips']))

    return response
