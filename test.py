# -*- coding: utf-8 -*-
import http.client, urllib
import json # 引入json库
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015','num':'1'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/it/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data) # 转换成字典
description = data["newslist"][0]["description"]
picUrl = data["newslist"][0]["picUrl"]
print(data["newslist"][0]["description"])
print(data["newslist"][0]["picUrl"])
