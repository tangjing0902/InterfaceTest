#-*- coding: UTF-8 -*-
import json
import os
import sys

__root_dir = os.path.abspath(os.path.dirname(__file__))
__root_dir = os.path.abspath(os.path.join(__root_dir, '..'))
os.environ['ET_INSTALLED_DIR'] = __root_dir
sys.path.insert(0, __root_dir)
egg_path = os.path.join(__root_dir, 'utlis')
sys.path.insert(0, egg_path)
from utlis.handlle_json import handle_json

class MockServer:
    '''
    flow.request.host
    http请求host
    flow.request.method
    请求方法
    flow.request.scheme
    请求协议
    flow.request.url
    请求URL链接
    flow.request.query
    请求URL查询参数
    flow.request.path
    请求URL路径
    flow.request.urlencoded_form
    请求POST数据
    flow.response.status_code
    HTTP响应状态码
    flow.response.headers
    HTTP响应头信息
    flow.response.get_text
    HTTP响应内容'''

    def request(self,flow):
        # 获取请求对象
        request = flow.request
        self.request_url = flow.request.url
        # 实例化输出类
        # 打印请求的url
        # print("url------------------------>",str(request.url).split("?")[0])
        # # 打印请求方法
        # print("method------------------------>",request.method)
        # # 打印host头
        # print("host------------------------>",request.host)
        # # 打印请求端口
        # print("port------------------------>",str(request.port))
        # # 打印所有请求头部
        # print("headers------------------------>",str(request.headers))
        # # 打印cookie头
        # print("cookies------------------------>",str(request.cookies))
        # #请求协议
        # print("scheme------------------------>",str(request.scheme))
        # #请求URL查询参数
        # print("query------------------------>",str(request.query))
        # # 请求URL路径
        # print("path------------------------>",str(request.path))
        # #请求POST数据
        # print("urlencoded_form------------------------>",str(request.urlencoded_form))
        # #HTTP响应状态码
        # # print("status_code------------------------>",str(request.status_code))
        # #HTTP响应内容
        # print("get_text------------------------>",str(request.get_text))

    def response(self, flow):
        response_data = flow.response

        url_path="apis.juhe.cn"
        if url_path in self.request_url:

            print("self.request_url-------------->",self.request_url)

            host = self.request_url.split(".cn/")[1]
            if not host.startswith("/"):
                host="/"+host
            if "?" in host:
                url = host.split("?")[0]

                data = handle_json.get_data_value("config/user_data.json",url)
                print("读取的数据：------------->",data)
            print("数据:---------------------->",response_data)
            response_data.set_text(json.dumps(data))

addons = [
            MockServer()
        ]

if __name__ == '__main__':
    url = "http://apis.juhe.cn/cook/query?key=d5d1a3b1642c6e385e939316d46a76a1&menu=%E8%A5%BF%E7%93%9C"
    print(url.split(".cn/")[1].split("?")[0])