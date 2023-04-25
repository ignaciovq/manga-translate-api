import os


def clearFiles(filename, clipLength):
    name, ext = os.path.splitext(filename)

    try:
        os.remove(f"assets/imagesToProcess/{filename}")
        os.remove(f"assets/processedImagesData/{name}.json")
        os.remove(f"assets/processedImagesData/mask-{name}.png")
        os.remove(f"assets/processedImagesData/{name}.png")
        os.remove(f"assets/processedImagesData/{name}.txt")
        os.remove(f"assets/processedImagesData/line-{name}.txt")

        for i in range(0, clipLength):
            os.remove(f"assets/imageClips/mask-{name}{i}.png")

    except Exception as e:
        print(e)
