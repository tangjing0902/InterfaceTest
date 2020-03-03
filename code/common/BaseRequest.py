#-*- coding: UTF-8 -*-
import requests
from utlis.handle_cookie import handle_cookie
class BaseRequest(object):


    def __init__(self):
        pass


    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        print("=======")
        print(header)
        res = requests.get(url=url, params=data, cookies=cookie, headers=header)

        if get_cookie!=None:
            cookie_value_jar = res.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            handle_cookie.write_cookie(cookie_value,get_cookie["is_cookie"])
        return res.text

    def send_post(self, url, data, cookie=None,get_cookie=None, header=None):
        res = requests.post(url=url, data=data, cookies=cookie, headers=header)
        return res.text

    def send_request(self,method, url, data, cookie=None, get_cookie=None,header=None):
        if method=="get":
         return self.send_get(url,data,cookie,get_cookie,header)
        else:
         return self.send_post(url, data, cookie,get_cookie, header)


base_request = BaseRequest()