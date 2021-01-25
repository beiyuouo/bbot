# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/25 13:34
# Description:

import httpx


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
        self.china_str = f"国内疫情：截止至{data['lastUpdateTime']}\n" \
                         f"新增确诊{chinaTotalToday['confirm'] - chinaTotalToday['heal'] - chinaTotalToday['dead']}例，" \
                         f"新增治愈{chinaTotalToday['heal']}例，" \
                         f"新增死亡{chinaTotalToday['dead']}例，" \
                         f"新增无症状{chinaTotalExtdata['incrNoSymptom']}例\n" \
                         f"现有确诊{chinaTotalTotal['confirm'] - chinaTotalTotal['heal'] - chinaTotalTotal['dead']}例，" \
                         f"境外输入{chinaTotalTotal['input']}例，" \
                         f"无症状{chinaTotalExtdata['noSymptom']}例\n" \
                         f"累计确诊{chinaTotalTotal['confirm']}例，" \
                         f"累计治愈{chinaTotalTotal['heal']}例，" \
                         f"累计死亡{chinaTotalTotal['dead']}例\n\n"
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
            todayConfirm += int(area['today']['confirm'] if area['today']['confirm'] is not None else 0)
            todayHeal += int(area['today']['heal'] if area['today']['heal'] is not None else 0)
            todayDead += int(area['today']['dead'] if area['today']['dead'] is not None else 0)

            totalConfirm += int(area['total']['confirm'] if area['total']['confirm'] is not None else 0)
            totalHeal += int(area['total']['heal'] if area['total']['heal'] is not None else 0)
            totalDead += int(area['total']['dead'] if area['total']['dead'] is not None else 0)

            existConfirm += totalConfirm - totalHeal - totalDead

        self.total_str = f"国际疫情：截止至{data['overseaLastUpdateTime']}\n" \
                         f"新增确诊{todayConfirm}例，新增治愈{todayHeal}例，新增死亡{todayDead}例\n" \
                         f"现存确诊{existConfirm}例，累计确诊{totalConfirm}例，累计死亡{totalDead}例"
        self.overseaUpdateTime = data['overseaLastUpdateTime']
        return self.total_str

    def calc_sum(self, data: dict):
        todayConfirm = int(data['today']['confirm'] if data['today']['confirm'] is not None else 0)
        todayHeal = int(data['today']['heal'] if data['today']['heal'] is not None else 0)
        todayDead = int(data['today']['dead'] if data['today']['dead'] is not None else 0)

        totalConfirm = int(data['total']['confirm'] if data['total']['confirm'] is not None else 0)
        totalHeal = int(data['total']['heal'] if data['total']['heal'] is not None else 0)
        totalDead = int(data['total']['dead'] if data['total']['dead'] is not None else 0)

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
        res = f"{city}疫情：截止至{data['lastUpdateTime']}\n" \
              f"新增确诊{todayConfirm}例，新增治愈{todayHeal}例，新增死亡{todayDead}例\n" \
              f"现存确诊{existConfirm}例，累计确诊{totalConfirm}例，累计死亡{totalDead}例"

        return res
        pass

    async def get_sum(self):
        json = await self.get_json()
        data = json['data']
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
