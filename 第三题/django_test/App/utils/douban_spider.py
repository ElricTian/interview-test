import datetime
import time
import requests
import pymongo
from lxml import etree


def get_html():
    url = 'https://movie.douban.com/cinema/nowplaying/xiamen/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'movie.douban.com'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    # print(response.status_code)
    return html


def parse_html(html):
    movies = []
    html = etree.HTML(html)
    ul = html.xpath("//ul[@class='lists']")[0]
    all_li = ul.xpath("./li")
    for li in all_li:
        title = li.xpath("@data-title")[0]
        director = li.xpath("@data-director")[0]
        actors = li.xpath("@data-actors")[0]
        score = li.xpath("@data-score")[0]
        release = li.xpath("@data-release")[0]
        duration = li.xpath("@data-duration")[0]
        region = li.xpath("@data-region")[0]
        buy_url = li.xpath("ul/li[@class='sbtn']/a/@href")[0]

        movie = {
            # 片名
            'title': title,
            # 导演 编剧
            'director': director,
            # 主演
            'actors': actors,
            # 地区
            'region': region,
            # 评分
            'score': score,
            # 上映时间
            'release': release,
            # 片长
            'duration': duration,
            # 购买链接
            'buy_url': buy_url
        }
        movies.append(movie)
    return movies


def save_data(document):
    # 连接服务器
    client = pymongo.MongoClient(host='localhost', port=27017)
    # 指定数据库
    db = client['spider']
    # 指定集合
    collection = db['douban_spider']

    result = collection.insert(document)
    if result:
        print("存入数据库成")


def douban_spider():
    html = get_html()
    document = parse_html(html)
    save_data(document)


def timing(h):

    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        if now.hour == h:
            print('开始运行爬虫程序')
            douban_spider()
            print("已爬取完")
        time.sleep(60)


if __name__ == '__main__':
    # douban_spider()
    timing(9)
