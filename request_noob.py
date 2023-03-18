"""
request模块，网络请求模块。功能强大、简单便捷、效率高
模拟浏览器发送请求
"""
import requests

url = "https://www.sogou.com/"  # 需要get爬数据的url
post_url = "https://www.sogou.com/"  # 需要post爬数据的url
Headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}  # ua伪装


def request_get():
    params = {
        "cname": "",
        "pid": "",
        "keyword": "上海",
        "pageIndex": 1,
        "pageSize": "10"
    }  # get请求参数
    response = requests.get(url=url, params=params, headers=Headers)
    page_text = response.text  # 页面数据
    json_data = response.json()  # json数据


def request_post():
    # url携带的参数封装到字典
    data = {
        "kw": "dog"
    }
    response = requests.post(url=post_url, data=data, headers=Headers)
    page_text = response.text
    json_data = response.json()
    print(json_data)


if __name__ == "__main__":
    ...
