import random
from time import time, localtime
import cityinfo
from requests import get, post
from datetime import datetime, date
import sys
import os
import http.client, urllib
import json
from zhdate import ZhDate
def get_color():
    # 获取随机颜色
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)

def get_access_token():
    # appId
    app_id = config["app_id"]
    # appSecret
    app_secret = config["app_secret"]
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    try:
        access_token = get(post_url).json()['access_token']
    except KeyError:
        print("获取access_token失败，请检查app_id和app_secret是否正确")
        os.system("pause")
        sys.exit(1)
    # print(access_token)
    return access_token
def get_weather(province, city):
    # 城市id
    try:
        city_id = cityinfo.cityInfo[province][city]["AREAID"]
    except KeyError:
        print("推送消息失败，请检查省份或城市是否正确")
        os.system("pause")
        sys.exit(1)
    # city_id = 101280101
    # 毫秒级时间戳
    t = (int(round(time() * 1000)))
    headers = {
        "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
    response = get(url, headers=headers)
    response.encoding = "utf-8"
    response_data = response.text.split(";")[0].split("=")[-1]
    response_json = eval(response_data)
    # print(response_json)
    weatherinfo = response_json["weatherinfo"]
    # 天气
    weather = weatherinfo["weather"]
    # 最高气温
    temp = weatherinfo["temp"]
    # 最低气温
    tempn = weatherinfo["tempn"]
    return weather, temp, tempn

#下雨概率和建议
def tip():
    if (tianqi_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianqi_API,'city':city})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/tianqi/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        pop = data["newslist"][0]["pop"]
        tips = data["newslist"][0]["tips"]
        return pop,tips
    else:
        return "",""
# 早安心语
def gm():
    if (tianqi_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
        params = urllib.parse.urlencode({'key': '958c64cb1c216f910a6126540c25a015'})
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        conn.request('POST', '/zaoan/index', params, headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)  # 转换成字典
        gm = data["newslist"][0]["content"]
        return gm
    else:
        return ""
# 笑话
def joke():
    if (tianqi_API != "否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
        params = urllib.parse.urlencode({'key': '958c64cb1c216f910a6126540c25a015', 'num': '1'})
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        conn.request('POST', '/joke/index', params, headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)  # 转换成字典
        joke_title = data["newslist"][0]["title"]
        joke_content = data["newslist"][0]["content"]
        return joke_title,joke_content
    else:
        return "",""
def it_index():
    if (it_index_API != "否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':'958c64cb1c216f910a6126540c25a015','num':'1'})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/it/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data) # 转换成字典
        description = data["newslist"][0]["description"]

        return description
    else:
        return ""

#推送信息
def send_message(to_user, access_token, city_name, weather, max_temperature, min_temperature,pop,tips,gm,joke_title,joke_content,description):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]

    data = {
        "touser": to_user,
        "template_id": config["template_id"],
        "url": "http://weixin.qq.com/download",
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": "{} {}".format(today, week),
                "color": get_color()
            },
            "city": {
                "value": city_name,
                "color": get_color()
            },
            "weather": {
                "value": weather,
                "color": get_color()
            },
            "min_temperature": {
                "value": min_temperature,
                "color": get_color()
            },
            "max_temperature": {
                "value": max_temperature,
                "color": get_color()
            },
            "pop": {
                "value": pop,
                "color": get_color()
            },
            "tips": {
                "value": tips,
                "color": get_color()
            },
            "gm": {
                "value": gm,
                "color": get_color()
            },
            "joke_title": {
                "value": joke_title,
                "color": get_color()
            },
            "joke_content": {
                "value": joke_content,
                "color": get_color()
            },
            "description": {
                "value": description,
                "color": get_color()
            }
            }
        }


    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
    else:
        print(response)
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    try:
        with open("./config.json", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)

    # 获取accessToken
    accessToken = get_access_token()
    # 接收的用户
    users = config["user"]
    # 传入省份和市获取天气信息
    province, city = config["province"], config["city"]
    weather, max_temperature, min_temperature = get_weather(province, city)
    # 获取早安心语API
    gm_API = config["gm_API"]
    # 获取joke API
    joke_API = config["joke_API"]
    # 获取天气预报API
    tianqi_API = config["tianqi_API"]
    # 获取it资讯API
    it_index_API = config["it_index_API"]
    # 下雨概率和建议
    pop, tips = tip()
    # 早安心语
    gm = gm()
    # joke
    joke_title,joke_content = joke()
    # it_index it资讯
    description = it_index()
    for user in users:
        send_message(user, accessToken, city, weather, max_temperature, min_temperature,pop,tips,gm,joke_title,joke_content,description)
    import time
    time_duration = 3.5
    time.sleep(time_duration)

