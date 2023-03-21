import requests
import re


def get_page_num(page_num):  # 多页爬虫
    page_list = [i * 25 for i in range(page_num)]
    return page_list


def get_page(page_num):  # 单个页面数据返回
    url = "https://movie.douban.com/top250"
    Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }  # ua伪装
    params = {
        "start": page_num,
        "filter": ""
    }
    response = requests.get(url=url, headers=Headers, params=params)
    # response.encoding = 'utf_8'
    page_text = response.text
    response.close()
    return page_text  # 页面数据


def data_process(page):  # 正则提取数据
    data = []
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<movie_name>.*?)</span>'
                     r'.*?<p class="">.*?导演: (?P<diretor>.*?)&nbsp.*?主演: (?P<actor>.*?)...<br>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)  # re.S排除换行符
    resault = obj.finditer(page)
    for i in resault:
        dict = {}
        dict['movie_name'] = i.group('movie_name')
        dict['diretor'] = i.group('diretor')
        dict['actor'] = i.group('actor')
        dict['num'] = i.group('num')
        data.append(dict)
    return data


if __name__ == '__main__':
    page_list = get_page_num(2)
    data = []
    for page_num in page_list:
        page_text = get_page(page_num)
        page_data = data_process(page_text)
        data.extend(page_data)
