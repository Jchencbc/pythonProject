"""
request模块，网络请求模块。功能强大、简单便捷、效率高
模拟浏览器发送请求
"""
import requests

if __name__ == "__main__":
    url = "https://www.sogou.com/"
    response = requests.get(url=url)
    page_text = response.text  # 页面数据
    if page_text:
        ...
    else:
        ...