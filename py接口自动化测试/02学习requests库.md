import  requests
r = requests.get( 'https://api.github.com/user' , auth=( 'user' ,  'pass' ))
print (r.headers[ 'content-type' ])
print (r.encoding)
print

1.URL 传递参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.text）

2.定制请求头
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.text)
//json.dumps转换为json
//json.loads转换为字典

3.复杂的 POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print (r.text)
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)

4.POST 一个多部分编码(Multipart-Encoded)的文件
url = 'http://httpbin.org/post'
files = {'file': open('jiekoucase.xlsx', 'rb')}
r = requests.post(url, files=files)
print(r.text)
print(r.status_code)
print(r.headers)
5.Response.raise_for_status() 来抛出异常
bad_r=requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()
6.Cookies
url='http://example.com/some/cookie/setting/url'
r=requests.get(url)
print(r.cookies)
7.发送你的 cookies 到服务器
url='http://httpbin.org/cookies'
cookies=dict(cookies_are='working')
r=requests.get(url,cookies=cookies)
print(r.text)

8.重定向与请求历史
r=requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
r=requests.get('http://github.com',allow_redirects=False)
print(r.status_code)
print(r.history)
r=requests.head('http://github.com',allow_redirects=True)
print(r.url)
print(r.history)
9.超时
requests.get(‘http://github.com',timeout=0.001)