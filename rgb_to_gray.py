from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir):
    try:
        image_file = Image.open(jpgfile)  # open colour image
        image_file = image_file.convert('L')  # convert image to black and white
        image_file.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    convertjpg(r'E:\workspace\win10\fork\dog32x32.png', r'.')
