import requests
url = 'https://wanandroid.com/user/login'

payload = {'username':'ymw001','password':'123456'}

s = requests.session()

re1 = s.post(url=url,data=payload)
print(re1.text)

url1 = 'https://wanandroid.com//user/lg/userinfo/json'
re2 = s.get(url=url1)
print(re2.text)