#-*- coding: UTF-8 -*-
import json
import os
import sys
__root_dir = os.path.abspath(os.path.dirname(__file__))
__root_dir = os.path.abspath(os.path.join(__root_dir, '..'))
os.environ['ET_INSTALLED_DIR'] = __root_dir
sys.path.insert(0, __root_dir)
utl_path = os.path.join(__root_dir, 'utlis')
if os.path.exists(utl_path):
    sys.path.insert(0, utl_path)
from utlis.handlle_json import handle_json



class MockServer(object):



    #拦截请求
    def request(self, flow):
        request = flow.request
        self.request_data = request.url
        pass


    #拦截响应
    def response(self, flow):
        host  = "apis.juhe.cn"
        file_name="config/user_data.json"
        response_data = flow.response

        if host in self.request_data :
            if ".com/" in self.request_data:
                url = self.request_data.split(".com/")[1]
            else:
                url= self.request_data.split(".cn/")[1]
            url = url.split("?")[0]
            if not url.startswith("/"):
                url ="/"+url
            data = handle_json.get_data_value(file_name,url)
            response_data.set_text(json.dumps(data))


addons = [
            MockServer()
        ]
