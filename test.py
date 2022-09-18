# # -*- coding: utf-8 -*-
# import http.client, urllib
# import json # 引入json库
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015','num':'1'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/it/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data) # 转换成字典
# description = data["newslist"][0]["description"]
# picUrl = data["newslist"][0]["picUrl"]
# print(data["newslist"][0]["description"])
# print(data["newslist"][0]["picUrl"])

# import http.client, urllib
# import json
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/zaoan/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data) # 转换成字典
# print(data["newslist"][0]["content"])


# 特殊格式待学习
# import http.client, urllib
# import json
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/ncov/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# # data = json.loads(data) # 转换成字典
# # print(data["newslist"][0]["news"])

# print(data.decode('utf-8'))
import http.client, urllib
import json
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015','num':'1'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/joke/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data) # 转换成字典
print(data["newslist"][0]["title"])
print(data["newslist"][0]["content"])
# print(data.decode('utf-8'))