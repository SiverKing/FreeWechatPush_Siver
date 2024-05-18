开源微信推送

这是一个开源的基于Python的定时微信测试号公众号的推送程序

功能：使用微信测试号给多为用户定时发送推送消息，可自行改动消息规则或套用模板发送早安提醒

部署：将index.py 与城市id文件放至同一文件夹下，在本地或服务器或部署至github(需要自行部署)运行index文件均可，设置好定时时间时间一到便会自动执行推送程序

微信获取测试号ID，模板ID，用户ID，同时使用我的模板或者自行更改部分程序重新调整模板
#微信测试号模板
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
