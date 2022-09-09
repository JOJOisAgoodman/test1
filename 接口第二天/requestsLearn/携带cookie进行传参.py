import requests
url = 'https://wanandroid.com/user/login'

payload = {'username':'ymw001','password':'123456'}

re = requests.post(url=url,data=payload)

print(re.text)
print(re.headers)

cookie = re.cookies

url1 = 'https://wanandroid.com//user/lg/userinfo/json'
re1 = requests.get(url=url1,cookies=cookie)

print(re1.text)
print(re.cookies)