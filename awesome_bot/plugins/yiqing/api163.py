# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/25 13:34
# Description:

import httpx


def deal_none_int(data):
    if data is None:
        return 0
    else:
        return int(data)


def deal_none_str(data: str):
    if data is None:
        return ""
    else:
        return str(data)


class YiQing(object):
    url = 'http://c.m.163.com/ug/api/wuhan/app/data/list-total'
    updateTime = ""
    overseaUpdateTime = ""
    cityUpdateTime = ""
    citys = {}

    async def get_json(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        async with httpx.AsyncClient() as client:
            resp = await client.get(self.url, headers=headers)
            return resp.json()

    async def get_china(self, data: dict):
        if data['lastUpdateTime'] == self.updateTime:
            return self.china_str
        chinaTotal = data['chinaTotal']
        chinaTotalToday = chinaTotal['today']
        chinaTotalTotal = chinaTotal['total']
        chinaTotalExtdata = chinaTotal['extData']
        if not chinaTotalExtdata.get('noSymptom'):
            chinaTotalExtdata['noSymptom'] = 0

        if not chinaTotalExtdata.get('incrNoSymptom'):
            chinaTotalExtdata['incrNoSymptom'] = 0

        # print(deal_none(data['lastUpdateTime']))
        # print(f"{deal_none(data['lastUpdateTime'])}")
        self.china_str = f"国内疫情：截止至{deal_none_str(data['lastUpdateTime'])}\n" \
                         f"新增确诊{deal_none_int(chinaTotalToday['confirm']) - deal_none_int(chinaTotalToday['heal']) - deal_none_int(chinaTotalToday['dead'])}例，" \
                         f"新增治愈{deal_none_int(chinaTotalToday['heal'])}例，" \
                         f"新增死亡{deal_none_int(chinaTotalToday['dead'])}例，" \
                         f"新增无症状{deal_none_int(chinaTotalExtdata['incrNoSymptom'])}例\n" \
                         f"现有确诊{deal_none_int(chinaTotalTotal['confirm']) - deal_none_int(chinaTotalTotal['heal']) - deal_none_int(chinaTotalTotal['dead'])}例，" \
                         f"境外输入{deal_none_int(chinaTotalTotal['input'])}例，" \
                         f"无症状{deal_none_int(chinaTotalExtdata['noSymptom'])}例\n" \
                         f"累计确诊{deal_none_int(chinaTotalTotal['confirm'])}例，" \
                         f"累计治愈{deal_none_int(chinaTotalTotal['heal'])}例，" \
                         f"累计死亡{deal_none_int(chinaTotalTotal['dead'])}例\n\n"
        self.updateTime = data['lastUpdateTime']
        return self.china_str

    async def get_total(self, data: dict):
        if data['overseaLastUpdateTime'] == self.overseaUpdateTime:
            return self.total_str
        todayConfirm = 0
        todayHeal = 0
        todayDead = 0
        existConfirm = 0
        totalConfirm = 0
        totalHeal = 0
        totalDead = 0
        for area in data['areaTree']:
            # print(area)
            # print('-'*20)
            todayConfirm += deal_none_int(area['today']['confirm'])
            todayHeal += deal_none_int(area['today']['heal'])
            todayDead += deal_none_int(area['today']['dead'])

            totalConfirm += deal_none_int(area['total']['confirm'])
            totalHeal += deal_none_int(area['total']['heal'])
            totalDead += deal_none_int(area['total']['dead'])

            existConfirm += totalConfirm - totalHeal - totalDead

        self.total_str = f"国际疫情：截止至{deal_none_str(data['overseaLastUpdateTime'])}\n" \
                         f"新增确诊{todayConfirm}例，新增治愈{todayHeal}例，新增死亡{todayDead}例\n" \
                         f"现存确诊{existConfirm}例，累计确诊{totalConfirm}例，累计死亡{totalDead}例"
        self.overseaUpdateTime = data['overseaLastUpdateTime']
        return self.total_str

    def calc_sum(self, data: dict):
        todayConfirm = deal_none_int(data['today']['confirm'])
        todayHeal = deal_none_int(data['today']['heal'])
        todayDead = deal_none_int(data['today']['dead'])

        totalConfirm = deal_none_int(data['total']['confirm'])
        totalHeal = deal_none_int(data['total']['heal'])
        totalDead = deal_none_int(data['total']['dead'])

        existConfirm = totalConfirm - totalHeal - totalDead
        return todayConfirm, todayHeal, todayDead, existConfirm, totalConfirm, totalHeal, totalDead

    async def query_city(self, city: str, data: dict):
        if self.cityUpdateTime == data['lastUpdateTime']:
            return self.citys[city]

        todayConfirm = 0
        todayHeal = 0
        todayDead = 0
        existConfirm = 0
        totalConfirm = 0
        totalHeal = 0
        totalDead = 0
        flag = False
        dataChina = []
        for dt in data['areaTree']:
            if dt['name'] == city:
                todayConfirm, todayHeal, todayDead, existConfirm, totalConfirm, totalHeal, totalDead \
                    = self.calc_sum(dt)
                flag = True
            if dt['name'] == '中国':
                dataChina = dt
            if flag:
                break
        if not flag:
            for dt in dataChina['children']:
                if dt['name'] == city:
                    todayConfirm, todayHeal, todayDead, existConfirm, totalConfirm, totalHeal, totalDead \
                        = self.calc_sum(dt)
                    flag = True
                    break
                for child in dt['children']:
                    if child['name'] == city:
                        todayConfirm, todayHeal, todayDead, existConfirm, totalConfirm, totalHeal, totalDead \
                            = self.calc_sum(dt)
                        flag = True
                        break
                if flag:
                    break
        if not flag:
            raise Exception("Data Not Found!")
        res = f"{city}疫情：截止至{deal_none_str(data['lastUpdateTime'])}\n" \
              f"新增确诊{todayConfirm}例，新增治愈{todayHeal}例，新增死亡{todayDead}例\n" \
              f"现存确诊{existConfirm}例，累计确诊{totalConfirm}例，累计死亡{totalDead}例"

        return res
        pass

    async def get_sum(self):
        json = await self.get_json()
        data = json['data']
        # print(data)
        self.merge_str = await self.get_china(data) + await self.get_total(data)
        return self.merge_str

    async def get_city(self, city: str):
        json = await self.get_json()
        data = json['data']
        try:
            str = await self.query_city(city, data)
            return str
        except Exception as e:
            return "无法得到该城市数据"
        pass
