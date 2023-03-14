import requests

# ua:user_agent 请求身份标识，模仿浏览器发起请求

if __name__ == "__main__":
    # UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    search_list = ["华为", "中兴", "小米"]
    for i in search_list:
        # url携带的参数封装到字典
        param = {
            "query": i
        }
        url = "https://www.sogou.com/web"
        response = requests.get(url=url, params=param, headers=headers)
        page_text = response.text
        print(page_text)

