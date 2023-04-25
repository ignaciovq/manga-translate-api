import os


def clear_files(filename, clip_length):

    try:
        os.remove(f"assets/imagesToProcess/{filename}.png")
        os.remove(f"assets/processedImagesData/{filename}.json")
        os.remove(f"assets/processedImagesData/mask-{filename}.png")
        os.remove(f"assets/processedImagesData/{filename}.png")
        os.remove(f"assets/processedImagesData/{filename}.txt")
        os.remove(f"assets/processedImagesData/line-{filename}.txt")

        for i in range(0, clip_length):
            os.remove(f"assets/imageClips/mask-{filename}{i}.png")

    except Exception as e:
        print(e)
