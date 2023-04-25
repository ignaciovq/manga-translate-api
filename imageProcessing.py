from PIL import Image
from singleton import Singleton
from manga_ocr import MangaOcr
import json
import os


def clipTextFromMask(filename):
    name, ext = os.path.splitext(filename)
    textClips = {'language': '', 'clips': []}

    with open(f"assets/processedImagesData/{name}.json", 'r') as file:
        data = json.load(file)
    print(len(data))

    mask = Image.open(f"assets/processedImagesData/mask-{name}.png")
    for index, obj in enumerate(data):
        if index == 0:
            textClips['language'] = obj['language']
        coordinates = obj['xyxy']
        x1, y1, x2, y2 = coordinates
        clipping = mask.crop((x1, y1, x2, y2))
        clipdir = f"assets/imageClips/mask-{name}{index}.png"
        clipping.save(clipdir)
        textClips['clips'].append((coordinates, clipdir))

    mask.close()
    return textClips


def getTextFromClips(ocr, clips):
    returnData = []

    for clip in clips:
        image = Image.open(clip[1])
        text = ocr(image)
        print(text)
        returnData.append({'text': text, 'coordinates': clip[0]})
        image.close()

    return returnData


class MangaOcrSingleton(MangaOcr, metaclass=Singleton):
    pass


def get_manga_ocr():
    ocr_instance = MangaOcrSingleton()
    return ocr_instance
