#coding=utf-8
import requests
import hashlib
import json
imooc = "imooc.com"
md5 = hashlib.md5()
md5.update(imooc.encode('utf-8'))
reps = md5.hexdigest()
print(reps)

data = str({
    'user':'11111'
})
md5.update(data.encode('utf-8'))
reps2 = md5.hexdigest()
print(reps2)

header = {
    'Host':'www.imooc.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Accept':'*/*',
    'Sec-Fetch-Site':'same-site',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Dest':'script',
    'Referer':'https://m.imooc.com/',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'token':reps2
}
res = requests.get("https://www.imooc.com/apiw/logo?callback=jQuery21007257106286773107_1625580046662&_=1625580046663",headers=header,verify=False).json()

print(res)

