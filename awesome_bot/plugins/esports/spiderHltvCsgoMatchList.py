# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/2/20 20:40
# Description:

import crawlertool as tool
import requests
from bs4 import BeautifulSoup
import datetime
import json
import time
from typing import List, Dict
import re


def text_format(text):
    return re.sub(r'\s+', "", text)


class SpiderHltvCsgoMatchList(tool.abc.SingleSpider):
    _MATCH_LIST_URL = "https://www.hltv.org/stats/matches?startDate={}&endDate={}"
    _DATE_LIST_HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "__cfduid=dcb5ec3517cfddb27f20af70894eee0191613786385; MatchFilter={%22active%22:false%2C%22live%22:false%2C%22stars%22:1%2C%22lan%22:false%2C%22teams%22:[]}; _ga=GA1.2.1655132908.1613786415; _gid=GA1.2.42551263.1613786415; _ia__v4=%7B%22v%22%3A0%2C%22r%22%3A%22CN%22%2C%22sportsbook%22%3A%5B%5D%7D; CookieConsent={stamp:%27sfk6fVm9lxy/jkKiasRrYxcgcD+gyGCCDkbSRYpxK/lbwDkjwJ20Lw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1613786426295%2Cregion:%27cn%27}; _fbp=fb.1.1613823921574.1278836507; cf_chl_rc_ni=1; cf_chl_2=8a46e5d7fe10345; cf_chl_prog=a17; cf_clearance=76bba8ae542014ac8e58f0f4e058e070e7830852-1613824331-0-150; outbrain_cid_fetch=true",
        "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }

    def running(self, start_date, end_date, retry=0) -> List[Dict]:
        result = []
        if retry > 3:
            print("error")
            return result

        # 格式化日期
        end_date_str = end_date.strftime("%Y-%m-%d")
        start_date_str = start_date.strftime("%Y-%m-%d")

        URL = self._MATCH_LIST_URL.format(start_date_str, end_date_str)
        print(URL)

        # 抓取比赛页面数据
        try:
            response = tool.do_request(URL, method="get", headers=self._DATE_LIST_HEADERS)
            print(response)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                info = soup.find("table", {"class": "stats-table matches-table no-sort"})
                # print(info)
                rows = info.find_all("tr")
                # print(info)
                for row in rows:
                    print(row)
                    if len(row.find_all("td")) == 0:
                        continue
                    result.append({"Date": text_format(row.find("td", {"class": "date-col"}).text),
                                   "Team 1": text_format(row.findAll("td", {"class": "team-col"})[0].text),
                                   "Team 2": text_format(row.findAll("td", {"class": "team-col"})[1].text),
                                   "Map": text_format(row.find("td", {"class": "statsDetail"}).text),
                                   "Event": text_format(row.find("td", {"class": "event-col"}).text)
                                   })
        except:
            return self.running(start_date, end_date, retry=retry + 1)
        return result


if __name__ == "__main__":
    print(SpiderHltvCsgoMatchList().running(
        start_date=datetime.datetime.today() + datetime.timedelta(days=0),  # 抓取开始日期
        end_date=(datetime.datetime.today() + datetime.timedelta(days=0))  # 抓取结束日期
    ))
