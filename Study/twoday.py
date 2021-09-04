#coding=utf-8
import requests
import json
#上传文件
# url='https://www.imooc.com/user/postpic'
download_url ='http://file.mukewang.com/apk/app/132/1622440338/imooc_8.0.7_10102001_android.apk?version=1622440342'
file = {
    "fileField":("test.jpg",open("D:/WorkSpace/ImoocInterface/test.jpg","rb"),"image/jpg"),
    "type":"1"
}
cookie = {
    "apsid":"FjZWI1Zjg2OWRhYWZkNTAxODY5ZWY2NTAzMjdkOTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODEyODkwOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGJlZWE3MTYwNjM0M2RhYmEzMjA5NjlmZWE2MDQ4NWJi6lXYYNxV2GA=MW"
}
# res = requests.post(url,files=file,cookies=cookie,verify=False).json()


res = requests.get(download_url)
# with open("tesr.apk","wb") as f:
#     f.write(res.content)
print(res)


# Content-Disposition: form-data; name="fileField"; filename="238327093_6e2d0e8c_1.jpg"
# Content-Type: image/jpeg	<file>
# Content-Disposition: form-data; name="type"	1

