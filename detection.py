from comicTextDetector.inference import model2annotations


def getBBoxesAndSaveToFile():
    img_dir = r'assets/imagesToProcess'
    model_path = r'comicTextDetector/data/comictextdetector.pt'
    save_dir = r'assets/processedImagesData'
    model2annotations(model_path, img_dir, save_dir, save_json=True)
