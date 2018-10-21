# -*- coding: gb2312 -*-
import pymysql

def create_databases():
    '''
    创建数据库
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE spider DEFAULT CHARACTER SET UTF8MB4")
    db.close()


def create_tables():
    '''
    创建表
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS article(id MEDIUMINT UNSIGNED AUTO_INCREMENT,date TEXT NOT NULL,title VARCHAR(100) NOT NULL,wechat_id VARCHAR(20) NOT NULL,url TEXT NOT NULL,cover_img TEXT NOT NULL,content TEXT NOT NULL,img TEXT NOT NULL,html MEDIUMTEXT NOT NULL,PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


if __name__ == '__main__':

    print('1-创建数据库  |  2-创建表')
    choose = input('请选择：')
    if choose == '1':
        create_databases()
    elif choose == "2":
        create_tables()
    else:
        print("选择有误")