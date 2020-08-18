import json

from PIL import Image
from pylab import *
os.chdir("./data")


def get_info():

    filename_list = os.listdir()
    all_json = []

    # 指定获取所以json文件文件名
    for i in filename_list:
        if os.path.splitext(i)[1] == ".json":
            all_json.append(i)
    x_list = []
    y_list = []
    for json_name in all_json:
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


def draw(xy):

    x, y = xy
    c = 0
    print(len(y))
    os.chdir("..")
    filename = 'data106'

    if not os.path.exists(filename):
        os.mkdir(filename)

    os.chdir('data')
    filename_list = os.listdir()

    all_img = []
    for i in filename_list:
        if os.path.splitext(i)[1] == ".jpg":
            all_img.append(i)

    for i in all_img:
        if c < 22:

            img_name = "img" + str(c*2) + ".jpg"
            im = array(Image.open(img_name))

            # 绘制图像
            imshow(im)
            a = (c+1)*106
            b = c * 106

            plot(x[b:a], y[b:a], '.')
            c += 1
            img = "../data106/" + str(c)
            savefig(img)
            show()


if __name__ == '__main__':

    xy = get_info()
    draw(xy)
