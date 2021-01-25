# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/25 17:53
# Description:

import pymysql
import os
from awesome_bot.config.config import config


class SQL:
    def __init__(self):
        self.SOUTI_HOST = config.souti_host
        self.SOUTI_USERNAME = config.souti_username
        self.SOUTI_PASSWORD = config.souti_password

    async def get_connection(self):
        print(self.SOUTI_HOST, self.SOUTI_USERNAME, self.SOUTI_PASSWORD)
        self.db = pymysql.connect(host=self.SOUTI_HOST, port=3306, user=self.SOUTI_USERNAME,
                                  passwd=self.SOUTI_PASSWORD, db="qb", charset='utf8')
        self.cursor = self.db.cursor()
        return self.db, self.cursor

    async def query_dt(self, question: str):
        sql = f"SELECT q_title, q_answer FROM QuestionBank WHERE q_title like '%{question}%' LIMIT 3"
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            answers = ""
            for row in results:
                # print(row)
                answer = "问题：" + row[0] + "\n答案: " + row[1]
                answers += str(answer) + "\n"
            return answers
        except:
            print("Error: unable to fecth data")

    async def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    sql = SQL()
    sql.get_connection()
    sql.query_dt('马克思')
    sql.close()
