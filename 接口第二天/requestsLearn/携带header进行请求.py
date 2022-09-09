import requests
url = 'https://wanandroid.com/user/login'

payload = {'username':'ymw001','password':'123456'}

re = requests.post(url=url,data=payload)

print(re.text)

cookie = re.cookies
header = {}
header['Cookie'] = 'JSESSIONID=117A84D81A138FF2C167220BF53A5995'

url1 = 'https://wanandroid.com//user/lg/userinfo/json'
re2 = requests.get(url=url1,headers=header)

print(re2.text)