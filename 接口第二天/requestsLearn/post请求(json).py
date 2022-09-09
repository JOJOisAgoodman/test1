# 导包
import requests,json

# 准备接口
url = 'http://httpbin.org/post'

#准备数据
payload = {'username':'ymw001','password':'123456'}

# payload1 = json.dumps(payload)
#
# print(type(payload1))
#
# re = requests.post(url=url,data=payload1)

re = requests.post(url=url,json=payload)

print(re.text)
print(re.status_code)