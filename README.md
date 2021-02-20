![plugins-for-nonebot2](https://socialify.git.ci/beiyuouo/plugins-for-nonebot2/image?font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars0.githubusercontent.com%2Fu%2F44976445%3Fs%3D460%26u%3D182d335f502ab38522bde613717bd77aa1f6f766%26v%3D4&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)

<details>
    <summary>Click to open TOC</summary>

<!-- MarkdownTOC -->

- [Plugins for nonebot2](#plugins-for-nonebot2)
- [Changelog](#changelog)
    - [20210216 v0.1.3](#20210216-v013)
    - [20210125 v0.1.1-v0.1.2](#20210125-v011-v012)
    - [20210122 v0.1.0](#重要更新)
    - [20210116 v0.0.4](#20210116-v004)
    - [20210114 v0.0.3](#20210114-v003)
    - [20210114 v0.0.2](#20210114-v002)
    - [20210113 v0.0.1](#20210113-v001)
- [TODO](#todo)
- [插件说明](#%E6%8F%92%E4%BB%B6%E8%AF%B4%E6%98%8E)
    - [menu](#menu)
    - [base](#base)
    - [rp](#rp)
    - [ssr/v2ray](#ssrv2ray)
    - [v2raycs](#v2raycs)
    - [twqd](#twqd)
    - [ai](#ai)
    - [ai_100000000](#ai_100000000)
    - [bullshit](#bullshit)
    - [zhihu](#zhihu)
    - [twqh](#twqh)
    - [auto_agree](#auto_agree)
    - [setu](#setu)
    - [helpme](#helpme)
    - [souti](#souti)
    - [tiangou](#tiangou)
    - [weather](#weather)
    - [mrwh](#mrwh)
    - [yiqing](#yiqing)
    - [hhsh](#hhsh)
    - [esports](#esports)

<!-- /MarkdownTOC -->

</details>



## Plugins for nonebot2

自用插件（确信），测试机器人QQ851722457

有啥好的插件想法/独家定制请发issue 0.0

项目分为两个分支，`main`为稳定版本的分支，`dev`为正在开发的内容

## Changelog

### 20210220 v0.1.4
- 添加`love`插件

<details>
    <summary>Click to see more</summary>

### 20210216 v0.1.3
- 添加电竞查询插件

### 20210125 v0.1.1-v0.1.2
- 添加疫情查询插件
- 添加搜题插件

### 20210122 v0.1.0 [重要更新]
- 代码重构，更新配置方式，更易于移植和配置

### 20210116 v0.0.4
- 添加`hhsh`和`menu`功能

### 20210114 v0.0.3
- 仓库重命名为bbot

### 20210114 v0.0.2
- 添加`menu,mrwh`和`setu`功能

### 20210113 v0.0.1
- 基础框架和功能

</details>

## TODO

- [x] 重构
- [x] 配置文件，易部署修改
- [x] 异常处理
- [ ] 命令的模糊匹配

## 插件说明

<details>
    <summary>Click to see more</summary>

### menu

说明：插件汇总，菜单

命令：`{ menu | 菜单 }`

### base
说明：基础命令，由于目前食用的nonebot2版本builtin插件有问题，因此做了简单的重写

命令：`{ say | echo } { text }`

### rp
说明：测试用插件，`(1,100)` 随机数

命令：今日人品

### ssr/v2ray
说明：获取一条ssr/v2ray链接，API配合<a href="https://github.com/QIN2DIM/V2RayCloudSpider">V2RayCloudSpider</a>食用

命令：`{ ssr | v2ray }`

食用指北：修改`.env.dev`内配置ssr/v2ray/v2raycs的api接口

### v2raycs
说明：获取ssr/v2ray余量信息，API配合<a href="https://github.com/QIN2DIM/V2RayCloudSpider">V2RayCloudSpider</a>食用

命令：`v2raycs`

### twqd
说明：HainanUniversity体温签到接口

命令：
```
twqd { 学号 }
twqdall
adduser { 学号 } { 密码 } { 邮箱 }
add { 学号 } # 以发送人QQ为键值
add { qq } { 学号 }
query { qq | 学号 } {}
```

食用指北：后端使用MySQL存储QQ-学号映射，API由<a href="https://github.com/QIN2DIM/CampusDailyAutoSign">ALKAID</a>提供
需要修改`.env.dev`的字段
```
ALKAID_HOST = "" # CHANGE ALKAIDAPI HOST
QQMAP_HOST = "" # CHANGE 数据库HOST
QQMAP_USERNAME = "" # CHANGE 数据库用户名
QQMAP_PASSWORD = "" # CHANGE 数据库密码

PLUGINS_PATH = "awesome_bot/plugins/hnu-temp-report-bot" # CHANGE 插件目录
GOCQ_PATH = "" # CHANGE GO-CQHTTP运行目录
EXCEPTION_ADMIN = [{"type": "group", "id": ""}] # type: group or private, id: qq for group 
# 如果需要输出异常进行监控，可以利用这个修改成QQ群号或是QQ号即可

AccessKeyId = "" # CHANGE OSS key
AccessKeySecret = "" # CHANGE OSS secret
bucket_name = "" # CHANGE OSS bucket
oss2.Bucket(auth, "", bucket_name) # CHANGE OSS host
```

ps: 对于HainanUnverisity的同学，可以将bot(851722457)拉到群中进行签到，bot会自动同意加群和好友请求. 如需twqdall，请联系superadmin(729320011,471591513)，进行信息录入

### ai
说明：百度UNIX2，图灵机器人接口

命令：`""`，正常对话即可

食用指北：修改`.env.dev`内的BAIDU_API_KEY等

### ai_100000000
说明：价值一个亿的AI核心代码，dddd

命令：`ai {}`


### bullshit
说明：狗屁不通生成器

命令：`{ bullshit | 狗屁不通 | 狗屁不通生成器 } { theme }`

### zhihu
说明：知乎日报

命令：`{ zhihu | 知乎 | 知乎日报 }`

### twqh
说明：来一句土味情话

命令：`{ twqh | 土味情话 | 情话 | 土味 | 来句土味 | 来句情话 | 来句土味情话 | 你爱我吗 | 爱我吗 }`

### auto_agree
说明：自动同意好友申请和加群邀请

### setu

说明：给俺来张瑟图！

命令：`{ setu | 瑟图 | 色图 | 来张瑟图 | 来张色图 }`

### helpme
On Developing...

说明：帮我

命令：
```
帮我骂人 @someone
```

食用指北：添加`脏话样本.txt`

### souti

说明：搜题

命令：
```
搜题 { 题目 }
```

食用指北：


### tiangou

On Developing

说明：来舔我

命令：

食用指北：


### weather

On Developing

说明：天气预报

命令：

食用指北：

### mrwh

说明：每日问好，用到的插件<a href="https://github.com/nonebot/plugin-apscheduler">https://github.com/nonebot/plugin-apscheduler</a>

命令：无

食用指北：
修改`.env.dev`文件中
```
MRWH_GROUP = [''] # 需要通知的群列表
MRWH_SPECIAL_USER = [''] # 需要特殊提醒的群成员
TIANQI_KEY = '' #Tianqi API Key
```


### yiqing

说明：疫情查询

命令：`疫情 { 地点 }`

### hhsh

说明：能不能好好说话？

命令：`hhsh { text text }`


### esports

On developing.

说明：查询近日赛程

命令：`{ [lol, LOL, csgo, CSGO] [date] }`

参考：<a href="https://github.com/ChangxingJiang/CxSpider">link</a>

依赖：`crawlertool, Python3.8`

</details>