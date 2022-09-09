import requests

# 准备接口
url = "https://www.kuaidi100.com/query"
#准备数据
payload = {'type':'shunfeng','postid':'SF1403785112909'}
# 进行请求big返回结果
re = requests.get(url=url,params=payload)
# 查看结果
# 状态码
print(re.status_code)
# 响应体
print(re.text)
print(re.cookies)
print(re.request)
print(re.url)
print(re.json())
print(type(re.text))
print(type(re.json()))