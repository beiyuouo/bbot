# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/10 20:22
# Description:


import pymysql
import os
from awesome_bot.config.config import config

USER_DIC = {}
RE_USER_DIC = {}
PLUGINS_PATH = ''

QQMAP_HOST = config.qqmap_host
QQMAP_USERNAME = config.qqmap_username
QQMAP_PASSWORD = config.qqmap_password


def create_tb():
    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS twqd")

    # 创建数据表SQL语句
    sql = """CREATE TABLE twqd (
                 QQ VARCHAR(12) NOT NULL primary key,
                 STUNUM VARCHAR(14) NOT NULL,
                 NAME VARCHAR(12),
                 SCHOOL VARCHAR(50),
                 UNIVERSITY VARCHAR(50)
                 );
                 """

    cursor.execute(sql)


def insert_dt():
    # SQL 插入语句
    sql = """INSERT INTO twqd(QQ,STUNUM,NAME,SCHOOL,UNIVERSITY)
                 VALUES ('{}', '{}', '{}', '{}', '{}')"""
    for qq in USER_DIC.keys():
        try:
            # 执行sql语句
            print(sql.format(qq, USER_DIC[qq], '', '', ''))
            cursor.execute(sql.format(qq, USER_DIC[qq], '', '', ''))
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            print(qq, USER_DIC[qq])
            print('FAILED')
            db.rollback()


def query_dt():
    # SQL 查询语句
    sql = "SELECT * FROM twqd"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fecth data")


def main():
    # 打开数据库连接
    global db
    db = pymysql.connect(host=QQMAP_HOST, port=3306, user=QQMAP_USERNAME,
                         passwd=QQMAP_PASSWORD, db="cpds_db", charset='utf8')

    # 使用cursor()方法获取操作游标
    global cursor
    cursor = db.cursor()

    # create_tb()
    # insert_dt()
    # query_dt()

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    main()
