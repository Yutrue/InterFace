import requests
# import json

get_url = 'https://www.imooc.com/apiw/logo?callback=jQuery21007677720127275083_1623591391133&_=1623591391134'

url = 'http://www.imooc.com/api3/updateversion'
data = {
    'uid': '0',
    'v_code': '5100',
    'v': '5.1.0',
    'plat_id': '2',
    'secrect': '',
    'type': '0',
    'app_id': '1',
    'uuid': '',
    'timestamp': '1623590024875',
    'cid': '0',
    'token': '93bccacf8e68c1b02d91547076f6ec1c'
}
# res = requests.post(url,data,verify=False)
# json_res = res.json()
# print(json.dumps(json_res,indent=2,ensure_ascii=False))

# res_text = requests.get(get_url,verify=False).text
# print(res_text)

res_text = requests.get(get_url, verify=False).json()

print()