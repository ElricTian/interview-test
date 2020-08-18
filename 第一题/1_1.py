import os
import json
from PIL import Image
path = 'data'
os.chdir(path)


def change_filename():

    filename_list = os.listdir()
    a = 0

    for i in filename_list:

        old_name = filename_list[a]

        if os.path.splitext(old_name)[1] == ".jpg":
            new_name = 'img' + str(a) + '.jpg'

        else:
            new_name = 'img' + str(a) + '.json'
        a += 1
        os.rename(old_name, new_name)
        print("文件%s重命名成功,新的文件名为%s" % (old_name, new_name))


def get_info():

    filename_list = os.listdir()
    all_json = []

    # 指定获取json文件文件名
    for i in filename_list:
        if os.path.splitext(i)[1] == ".json":
            all_json.append(i)

    # 读取json提取信息
    boxes = []
    for json_name in all_json:
        json_file = open(json_name)
        info = json.load(json_file)
        face_box = info['stMobile106'][0]['face106']['rect']
        left, top, right, bottom = face_box['left'], face_box['top'], face_box['right'], face_box['bottom']
        box = (left, top, right, bottom)
        boxes.append(box)

    return boxes


def screenshots(boxes):

    b = 0
    c = 0
    os.chdir("..")
    filename = 'clip'

    # 如果没有该文件就创建该文件夹
    if not os.path.exists(filename):
        os.mkdir(filename)

    os.chdir('data')
    filename_list = os.listdir()
    for i in filename_list:
        if c < 40:
            img = Image.open("img" + str(c) + ".jpg")
            cropped = img.crop(boxes[b])
            img_name = "../clip/" + str(b) + ".jpg"
            cropped.save(img_name)
            c += 2
            b += 1


if __name__ == '__main__':
    change_filename()
    box = get_info()
    screenshots(box)
