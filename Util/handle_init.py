#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

# file_path = base_path+"/Config/server.ini"
# cf = configparser.ConfigParser()
# cf.read(file_path)
# data = cf.get('server','host')
# print(data)

class HandleInit:
    def load_ini(self):
        file_path = base_path+"/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf

    #获取ini里面的value
    def get_value(self,key,node=None):
        if node is None:
            node = 'server'

        cf = self.load_ini()   # return到server.ini的数据

        try:
            data = cf.get(node,key)
        except Exception:
            print("没有获取到值")
            data = None
        return data             

handdle_ini = HandleInit()


if __name__ == "__main__":
    hi = HandleInit()
    print(hi.get_value("password"))
