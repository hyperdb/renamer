#
#
#
import glob
import os
import random
import string
import shutil
from PIL import Image


def random_name(n=32):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def renamer(src_image):
    file_info = os.stat(src_image)

    src_name = os.path.basename(src_image)
    src_ext = os.path.splitext(src_name)[1]
    target_name = str(int(file_info.st_ctime)) + random_name(6) + src_ext

    return shutil.move(src_image, os.path.join("./dist", target_name))


def watermark(src_image):
    original = Image.open(src_image)
    stamp = Image.open(os.path.join("./watermarked", "stamp.png"))

    stamp.putalpha(64)
    stamp = stamp.resize((64, 64))

    x = original.width - stamp.width
    y = original.height - stamp.height

    original.paste(stamp, (x, y), stamp)
    original.save(src_image.replace("dist", "watermarked"))


def main(src_image):

    result_path = renamer(src_image)
    # watermark(result_path)
    print(result_path)


if __name__ == "__main__":

    src_images = glob.glob(os.path.join("./src", "*.*"))

    for src_image in src_images:
        main(src_image)
