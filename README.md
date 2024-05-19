# 免费微信推送
原理：申请免费的测试版公众号，可获得免费的模板推送功能。

### 视频教程

敬请期待

作者 **Siver**或**SiverKing** 全网同名，转载请注明作者，README.md修改自**技术爬爬虾**(bilibili)

### 申请公众号测试账户

使用微信扫码即可
https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

进入页面以后我们来获取到这四个值 
#### appID  appSecret openId template_id
![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/bdb27abd-39cb-4e77-9b89-299afabc7330)
图片来源**技术爬爬虾**

想让谁收消息，谁就用微信扫二维码，然后出现在用户列表，获取微信号（openId）
 ![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/1327c6f5-5c92-4310-a10b-6f2956c1dd75)
图片来源**技术爬爬虾**

新增测试模板获得  template_id（模板ID）
 ![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/ec689f4d-6c0b-44c4-915a-6fd7ada17028)
图片来源**技术爬爬虾**

模板标题随便填，模板内容如下，可以根据需求自己定制

模板一 ：
```copy
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
```


### 配置代码

将上面获得的几个值填入代码这几行,同时修改对应用户的城市与他想要接收的生日倒计时

![2](https://github.com/SiverKing/FreeWechatPush_Siver/assets/112841633/300532d1-2224-4c96-ab7e-3b535c97c078)

### 配置定时任务

修改这几行里的时间
![2](https://github.com/SiverKing/FreeWechatPush_Siver/assets/112841633/356aba83-8383-4266-955f-0bdae56d9cb6)

最后将ChengShi_id.py 和 index.py放置同一目录下 在本地电脑或服务器运行index.py即可
### 安装python依赖，启动项目
```copy
pip3 install requests html5lib bs4 schedule
```
