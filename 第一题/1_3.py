import json
import os
from PIL import Image
from pylab import *


def get_info():
    os.chdir("./data")
    filename_list = os.listdir()
    all_json = []

    # 指定获取所以json文件文件名
    for i in filename_list:
        if os.path.splitext(i)[1] == ".json":
            all_json.append(i)

    # 列表排序
    new_list = sorted(all_json, key=lambda x:int(re.match(r'(\d+)', x).group()))

    x_list = []
    y_list = []
    for json_name in new_list:
        json_file = open(json_name)
        info = json.load(json_file)
        points = info['stMobile106'][0]['face106']['pointsArray']

        for point in points:
            x = point['x']
            y = point['y']
            x_list.append(x)
            y_list.append(y)

    xy = [x_list, y_list]
    return xy


def draw2(xy):

    x, y = xy
    c = 0

    os.chdir("..")
    filename = 'clip106'

    if not os.path.exists(filename):
        os.mkdir(filename)

    os.chdir('./clip')
    filename_list = os.listdir()

    all_img = []
    for i in filename_list:
        if os.path.splitext(i)[1] == ".jpg":
            all_img.append(i)

    for i in all_img:

        img_name = str(c) + ".jpg"
        im = array(Image.open(img_name))

        # 绘制图像
        imshow(im)
        a = (c+1)*106
        b = c * 106

        plot(x[b:a], y[b:a], '.')

        img = "../clip106/" + str(c)
        savefig(img)
        show()
        c += 1


def re_size():

    os.chdir('./clip106')
    c = 0
    imgs = os.listdir()

    for i in imgs:
        im = str(c) + ".png"
        img = Image.open(im)  # 读取图片
        width = img.size[0]
        height = img.size[1]

        img_deal = img.resize((width*2, height*2), Image.ANTIALIAS)
        img_deal.save(im)
        c +=1


# xy = get_info()
# draw2(xy)
# re_size()
