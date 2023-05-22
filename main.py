from PIL import Image
from os import listdir


def repair_image(file_name):
    img = Image.open(f'./broken/{file_name}')
    img.save(f'./fixed/{file_name}')


if __name__ == '__main__':
    for file in listdir('./broken'):
        repair_image(file)

