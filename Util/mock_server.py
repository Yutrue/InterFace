# coding=utf-8
import sys
import os
import json
base_path = os.getcwd()
print(base_path)
# sys.path.append(base_path)
sys.path.append('D:\\WorkSpace\\ImoocInterface')

from mitmproxy import http
from Util.handle_json import get_value

class MockServer:
    def request(self,flow):
        request_data = flow.request
        self.request_url = request_data.url

        # request_data.host = '127.0.0.1'
        # request_data.port = 5000
        # request_pr = request_data.query
        # request_form = request_data.urlencoded_form
        # print("url------>",self.request_url)
        # print("request_pr------->",request_pr)
        # print("request_form------------->",request_form)

    def response(self,flow):
        if 'imooc' in self.request_url or 'mukewang' in self.request_url:

            response_data = flow.response
            
            url = self.request_url.split('.com/')[1]
            if '?' in url:
                url = url.split('?')[0]
            # print(url)
            data = json.dumps(get_value(url))
            # print(data)
            response_data.set_text(data)
            
addons = [
    MockServer()
]