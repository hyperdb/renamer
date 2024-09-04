#
#
#
import glob
import os
import random
import string
import shutil


def random_name(n=32):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def main(src_image):

    file_info = os.stat(src_image)

    src_name = os.path.basename(src_image)
    src_ext = os.path.splitext(src_name)[1]
    target_name = str(int(file_info.st_ctime)) + random_name(6) + src_ext

    result_path = shutil.move(src_image, os.path.join("./dist", target_name))

    print(result_path)


if __name__ == "__main__":

    src_images = glob.glob(os.path.join("./src", "*.*"))

    for src_image in src_images:
        main(src_image)
