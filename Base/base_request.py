#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_cookie import write_cookie
from Util.handle_init import handdle_ini
from Util.handle_json import get_value

# requests.post()
# requests.get()
class BaseRequest:
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        # res = requests.post(url=url,data=data,cookies=cookie).text
        # print(header)
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        # print(response)
        
        if get_cookie != None:
            #{"is_cookie":"yes"}
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        
        res = response.text
        return res

    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        # res = requests.get(url=url,params=data,cookies=cookie).text
        response = requests.get(url=url,params=data,cookies=cookie,headers=header)
        
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        
        res = response.text
        return res

    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):

        #return get_value(url)          #直接替换为user_data.json的数据，以下不执行

        base_url = handdle_ini.get_value('host')        #拿到server.ini的数据 host = http://www.imooc.com/
        
        if 'http' not in url:
            url = base_url+url

        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)

        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")

        return res  #拿到get/post后的响应值

request = BaseRequest()

if __name__ == "__main__":
    request = BaseRequest()
    # request.run_main('get','login','')
    #{'username':'test','password':'123456'}
