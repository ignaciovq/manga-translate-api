from PIL import Image
import json, os
from manga_ocr import MangaOcr


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


def getTextFromClips(clips):
    ocr = MangaOcr()
    returnData = []

    for clip in clips:
        image = Image.open(clip[1])
        text = ocr(image)
        print(text)
        returnData.append({'text': text, 'coordinates': clip[0]})
        image.close()

    return returnData
