import requests

# 准备接口
url = "https://wanandroid.com/user/login"
#准备数据
payload = {'username':'ymw001','password':'123456'}
# 进行请求big返回结果
re = requests.post(url=url,data=payload)
# 查看结果
# 状态码
print(re.status_code)
# 响应体
print(re.text)
