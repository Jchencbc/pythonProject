import requests
import re

Headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}  # ua伪装


def get_main_page():  # 抓去电影天堂主页面
    url = "https://www.dy2018.com/"
    response = requests.get(url=url, headers=Headers)
    response.encoding = 'gbk'
    page = response.text
    response.close()
    return page  # 页面数据


def main_page_process(page):  # 正则提取数据
    url_list = []
    obj = re.compile(r'<span style="float:left;">2023必看热片.*?<ul>(?P<html>.*?)</ul>', re.S)  # re.S排除换行符
    resault_main = obj.search(page)
    html = resault_main.group('html')
    obj_two = re.compile(r"<li><a href='(?P<urls>.*?)' title=", re.S)
    resault_url = obj_two.finditer(html)
    for url_data in resault_url:
        url_data = "https://www.dy2018.com" + url_data.group('urls')
        url_list.append(url_data)
    return url_list


def page_process(url_list):
    for url in url_list:
        response = requests.get(url=url, headers=Headers)
        response.encoding = 'gbk'
        page = response.text
        obj = re.compile(r'<br />◎片　　名(?P<name>.*?)<br />.*?<div id="downlist"(?P<magnet>.*?)</div>',
                         re.S)  # re.S排除换行符
        name = obj.search(page).group('name')
        magent_page = obj.search(page).group('magnet')
        resault = obj.finditer(page)
        ...  # 处理拿下载链接的逻辑，over！
        response.close()
        return


if __name__ == '__main__':
    page_text = get_main_page()
    url_list = main_page_process(page_text)
    page_process(url_list)
