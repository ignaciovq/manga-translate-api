import os
from fastapi import FastAPI, File, UploadFile, Depends
from PIL import Image
from io import BytesIO
from manga_ocr import MangaOcr
from detection import get_bboxes_and_save_to_file
from imageProcessing import clip_text_from_mask, get_text_from_clips, get_manga_ocr
from utils import clear_files
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/api/ocr")
async def ocr(file: UploadFile = File(...), ocr: MangaOcr = Depends(get_manga_ocr)):
    content = await file.read()

    file_name, extension = os.path.splitext(file.filename)

    image = Image.open(BytesIO(content))
    image.save(
        f"assets/imagesToProcess/{file_name}.png", format="png", lossless=True)
    image.close()

    get_bboxes_and_save_to_file()
    text_clips = clip_text_from_mask(file_name)
    text = get_text_from_clips(ocr, text_clips['clips'])

    response = {"filename": file.filename,
                "language": text_clips['language'], "result": text}

    clear_files(file_name, len(text_clips['clips']))

    return response
