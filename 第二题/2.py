import os
import xml.dom.minidom
import pandas as pd


def change_filename():

    os.chdir('./data')

    filename_list = os.listdir()
    a = 0
    for i in filename_list:

        old_name = filename_list[a]
        new_name = str(a) + '.xml'
        a += 1
        os.rename(old_name, new_name)
        print("文件%s重命名成功,新的文件名为%s" % (old_name, new_name))


def parse_xml():

    b = 0
    items = []
    os.chdir('./data')

    while b < 10:
        # 打开xml文档
        xml_file = str(b) + ".xml"
        dom = xml.dom.minidom.parse(xml_file)

        # 得到文档元素对象
        root = dom.documentElement
        bndbox = root.getElementsByTagName('bndbox')

        for box in bndbox:
            xmin = box.getElementsByTagName('xmin')[0].childNodes[0].data
            ymin = box.getElementsByTagName('ymin')[0].childNodes[0].data
            xmax = box.getElementsByTagName('xmax')[0].childNodes[0].data
            ymax = box.getElementsByTagName('ymax')[0].childNodes[0].data

            xmin = int(xmin)
            ymin = int(ymin)
            xmax = int(xmax)
            ymax = int(ymax)

            x = xmax - xmin
            y = ymax - ymin
            s = x*y
            item = {
                "xmin": xmin,
                "xmax": xmax,
                "ymin": ymin,
                "ymax": ymax,
                "s": s
            }
            items.append(item)
        b += 1
    return items


def count_num(items):
    df = pd.DataFrame(items)

    sum = df.sum().tolist()
    xmin_sum = 'xmin_sum:' + str(sum[0])
    ymin_sum = 'ymin_sum:' + str(sum[1])
    xmax_sum = 'xmax_sum:' + str(sum[2])
    ymax_sum = 'ymax_sum:' + str(sum[3])
    content = [xmin_sum, ymin_sum, xmax_sum, ymax_sum]

    s_avg = df['s'].mean().tolist()
    content.append(('s_avg:' + str(s_avg)))

    s_max = df['s'].max().tolist()
    content.append(('s_max:' + str(s_max)))

    s_var = df['s'].var().tolist()
    content.append(('s_var:' + str(s_var)))

    with open("2.txt", "w") as f:
        for i in content:
            f.write("{}\n".format(i))


if __name__ == '__main__':
    # change_filename()
    items = parse_xml()
    count_num(items)
