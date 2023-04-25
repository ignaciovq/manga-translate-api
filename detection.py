from comic_text_detector.inference import model2annotations


def get_bboxes_and_save_to_file():
    img_dir = r'assets/imagesToProcess'
    model_path = r'comic_text_detector/data/comictextdetector.pt'
    save_dir = r'assets/processedImagesData'
    model2annotations(model_path, img_dir, save_dir, save_json=True)
