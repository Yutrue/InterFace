#coding = utf-8
import json

str1 = "文字"
str2 = '{"data":"123456"}'

try:
    str1 = json.loads(str1)
except:
    print("zifchuan1")

str2 = json.loads(str2)
print(str2)

a = {'name':'alex','age':27}
print(json.dumps(a),type(json.dumps(a)))
a = 8
print(json.dumps(a),type(json.dumps(a)))