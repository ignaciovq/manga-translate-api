from PIL import Image
from singleton import Singleton
from manga_ocr import MangaOcr
import json


def clip_text_from_mask(filename):
    text_clips = {'language': '', 'clips': []}

    with open(f"assets/processedImagesData/{filename}.json", 'r') as file:
        data = json.load(file)
    print(len(data))

    mask = Image.open(f"assets/processedImagesData/mask-{filename}.png")
    for index, obj in enumerate(data):
        if index == 0:
            text_clips['language'] = obj['language']
        coordinates = obj['xyxy']
        x1, y1, x2, y2 = coordinates
        clipping = mask.crop((x1, y1, x2, y2))
        clip_dir = f"assets/imageClips/mask-{filename}{index}.png"
        clipping.save(clip_dir)
        text_clips['clips'].append((coordinates, clip_dir))

    mask.close()
    return text_clips


def get_text_from_clips(ocr, clips):
    return_data = []

    for clip in clips:
        image = Image.open(clip[1])
        text = ocr(image)
        print(text)
        return_data.append({'text': text, 'coordinates': clip[0]})
        image.close()

    return return_data


class MangaOcrSingleton(MangaOcr, metaclass=Singleton):
    pass


def get_manga_ocr():
    ocr_instance = MangaOcrSingleton()
    return ocr_instance
