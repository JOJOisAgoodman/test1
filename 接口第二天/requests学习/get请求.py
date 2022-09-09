import requests

# pip install requests
# setting-Python_interpreter-加号搜索requests


url = 'https://www.kuaidi100.com/query'

payload = {"type": "shunfeng", "postid": "SF1409812533378"}

re = requests.get(url=url, params=payload)

print(re.status_code)
print(re.text)
