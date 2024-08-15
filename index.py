# -*- coding: utf8 -*-
'''
Siver所有

微信测试号定时推送程序

首次提交:2024/05/18
作者:Siver
www.siverking.online
'''
#微信模板保存
'''
今日公历{{date0.DATA}}
中国{{date1.DATA}}
-{{date2.DATA}}
城市{{date3.DATA}}
-{{date4.DATA}}
天气情况{{date5.DATA}}
-{{date6.DATA}}
最低气温{{date7.DATA}}
-{{date8.DATA}}
最高气温{{date9.DATA}}
-{{date10.DATA}}
今天是我们恋爱的第{{love_day.DATA}}天
生日{{date11.DATA}}
-{{date12.DATA}}
每日金句{{date13.DATA}}
每日金句{{date14.DATA}}
'''
#用户列表 #以下ID均经过修改只是示例不可使用
User=[
    {
        'app_id' : 'wx666666666666666',
        'app_secret' : 'b6116ffa944de59d48409843d935486a',
        '用户列表' : [
            {
                '用户ID' : 'ozgrT6q1xqiNUG1wxlp4_6QJF_aQ',
                '模块ID' : 'qBN1lrHqyvI4fLtbsHKQ6DqzI_nbv4WrRBwQ1h6DWss',
                '省份' : '浙江',#对应另一个文件查找
                '城市' : '宁波',#对应另一个文件查找
                '生日' : {
                    '祯':'2004-1-1',
                    '威':'2004-1-1',
                    '博':'2004-1-1',
                    '铭':'2004-1-1',
                },
            },
            {
                '用户ID' : 'ozgrT6n4eo1xfS9BG6QBbl1GMZfk',
                '模块ID' : 'qBN1lrHqyvI4fLtbsHKQ6DqzI_nbv4WrRBwQ1h6DWss',
                '省份' : '浙江',#对应另一个文件查找
                '城市' : '宁波',#对应另一个文件查找
                '生日' : {
                    '铭':'2004-1-1',
                },
            },
        ]
    },
]
#end
import requests,time,datetime,ChengShi_id,random
import json
from bs4 import BeautifulSoup
import time
import schedule

def 生日距离天数计算(生日):
    生日 = 生日.split('-')
    dq=datetime.date.today()
    js=datetime.date(dq.year,int(生日[1]),int(生日[2]))
    if dq>js:
        js=datetime.date(dq.year+1,int(生日[1]),int(生日[2]))
        a = (js-dq).days
    elif dq<js:
        a = (js-dq).days
    else:
        a = '今'
    print('距离天数：%s'%a)
    return a

def 获取天气数据(城市id):
    headers = {
        'Referer': 'http://www.weather.com.cn/weather1d/%s.shtml'%城市id,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = 'http://d1.weather.com.cn/dingzhi/%s.html?_=%s'%(城市id,str(int(time.time() * 1000)))
    print(url)
    r = requests.get(url,headers=headers)
    r.encoding = 'utf-8'
    print(r.text)
    return eval(r.text.split(';')[0].split('=')[1])['weatherinfo']
#计算在一起的时间
def get_love_days():
    from time import localtime
    from datetime import datetime, date
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    love_date = date(2022, 12, 21)#在这修改在一起的日期
    # 获取在一起的日期差
    love_days = str(today.__sub__(love_date)).split(" ")[0]
    print(love_days)
    return love_days
#获取token
def get_access_token(app_id,app_secret):
    # 获取access token的url
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}' \
        .format(app_id.strip(), app_secret.strip())
    response = requests.get(url).json()
    print(response)
    access_token = response.get('access_token')
    return access_token
def 发送消息(app_id,app_secret,用户,city):
    显示内容=''
    #url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(app_id,app_secret)
    #print('url' + url)
    # 获取access token的url
    #access_token = requests.get(url).json()['access_token']
    access_token = get_access_token(app_id,app_secret)
    #print('登录令牌：' + access_token)
    
    week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六','星期日']
    时间=time.strftime('%Y年%m月%d日 %H:%M:%S（' + week_list[datetime.date.today().isoweekday()-1] + '）',time.localtime((int(time.mktime(time.gmtime()))+28800)))
    
    天气list = 获取天气数据(ChengShi_id.中国[用户['省份']][用户['城市']]['AREAID'])
    天气情况 = 天气list['weather']
    #weather = get_weather(city)
    #temp = weather[1]
    最高气温 = 天气list['temp']
    最低气温 = 天气list['tempn']

#    for 生日 in list(用户['生日'].keys()):
#        用户['生日'][生日]=生日距离天数计算(用户['生日'][生日])

    r = requests.get('http://open.iciba.com/dsapi/').json()
    英文文案=r['content']
    中文文案=r['note']

    r = requests.get('https://www.d5168.com/m/nongli.php',headers={'User-Agent':''},verify=False).text
    a=r.find('今日农历：')
    b=r.find('</font>',a)
    今日农历 = r[a:b]
    a=r.find('<p class="hm">')
    b=r.find('</p>',a)
    今日农历 += ' ' + r[a+14:b]
    
    for 生日 in list(用户['生日'].keys()):
        显示内容+='%s%s天 '%(生日, 生日距离天数计算(用户['生日'][生日]))
    print(用户['用户ID'])
    print(用户['模块ID'])
    print(用户['城市'])
    body = {
        'touser': 用户['用户ID'],
        'template_id': 用户['模块ID'],
        'url': 'http://www.baidu.com',
        'data': {
            "date0": {
                "value": '：'+时间
            },
            "date1": {
                "value": ':%s'%今日农历
            },
            "date2": {
                "value": ''
            },
            "date3": {
                "value": '：%s'%用户['城市']
            },
            "date4": {
                "value": ''
            },
            "date5": {
                "value": '：%s'%天气情况
            },
            "date6": {
                "value": ''
            },
            "date7": {
                "value": '：%s'%最低气温
            },
            "date8": {
                "value": ''
            },
            "date9": {
                "value": '：'+最高气温
            },
            "date10": {
                "value": ''
            },
            "love_day": {
                "value": get_love_days()
            },
            "date11": {
                "value": ' '+显示内容
            },
            "date12": {
                "value": ''
            },
            "date13": {
                "value": ':'+英文文案
            },
            "date14": {
                "value": ':'+中文文案
            }
        }
    }
    #显示内容+='今日公历：%s\n%s\n'%(时间,今日农历)
    #显示内容+='城市：%s\n'%用户['城市']
    #显示内容+='天气情况：%s\n'%天气情况
    #显示内容+='最低气温：%s\n'%最低气温
    #显示内容+='最高气温：%s\n'%最高气温
    #显示内容+='666\n\n'
    #for 生日 in list(用户['生日'].keys()):
        #显示内容+='距离%s的生日还有：%s天\n'%(生日,用户['生日'][生日])
    #显示内容+='\n'+英文文案+'\n'+中文文案+'\n'
    #显示内容list=显示内容.split('\n')
    #for a in range(len(显示内容list)):
        #body['data']['date%s'%a]={}
        #body['data']['date%s'%a]['value']=显示内容list[a]
        #data['data']['date%s'%a]['color']='#' + '%06x' % random.randint(0, 0xFFFFFF)
    print(str(body))
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    #url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + access_token
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print(requests.post(url, json.dumps(body)).text)
    #r = requests.post(url, headers=headers, json=data)
    #print(r.text)

def send():
    for 客户 in User:
        for 用户 in 客户['用户列表']:
            发送消息(客户['app_id'],客户['app_secret'],用户,'宁波')

#在此设置定时运行的时间
schedule.every().day.at("07:45").do(send)
#send()#测试时打开
while True:
        schedule.run_pending()
        time.sleep(1)



#模板保存
'''
今日公历{{date0.DATA}}
中国{{date1.DATA}}
-{{date2.DATA}}
城市{{date3.DATA}}
-{{date4.DATA}}
天气情况{{date5.DATA}}
-{{date6.DATA}}
最低气温{{date7.DATA}}
-{{date8.DATA}}
最高气温{{date9.DATA}}
-{{date10.DATA}}
今天是我们恋爱的第{{love_day.DATA}}天
生日{{date11.DATA}}
-{{date12.DATA}}
每日金句{{date13.DATA}}
每日金句{{date14.DATA}}
'''
