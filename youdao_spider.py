import requests

data = {
    "i": "code",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "salt":"16092072923229",
    "sign": "7d7cac75ed6b176f8a8c57644cbeae25",
    "lts": "1609207292322",
    "bv": "4f7ca50d9eda878f3f40fb696cce4d6d"
}


response = requests.post(url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule',
              data=data,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

print(1111)
print ((response.headers))
print (dir(response.request))
# 如果是json文件可以直接显示
print (response.text)
