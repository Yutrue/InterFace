#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

import MySQLdb

class GetMysql():
    def connect_db(self):
        # 打开数据库连接
        self.db = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8')

        # 使用cursor()方法获取操作游标 
        self.cursor = self.db.cursor()

    # 关闭数据库
    def close_db(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.db and self.cursor:
            self.cursor.close()
            self.db.close()
        return True

    def select_sql(self,sql):
        # SQL 查询语句
        #sql = "SELECT * FROM prize WHERE id=1"
        self.connect_db()
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        # print(results)
        return results

# sel_sql = GetMysql()

if __name__ == "__main__":
    hi = GetMysql()
    print(hi.select_sql("SELECT * FROM prize WHERE id=6"))