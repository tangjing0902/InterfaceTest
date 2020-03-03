# -*- coding: UTF-8 -*-
from utlis.handlle_json import handle_json
class handle_cookie(object):


    cookie_file_path="config/cookie.json"



    def get_cookie_value(self,key):
        return handle_json.get_data_value(self.cookie_file_path,key)



    def write_cookie(self,data,key):
        cookie_data = handle_json.read_json(file_name=self.cookie_file_path)
        cookie_data[key]=data
        handle_json.write_json(cookie_data,file_name=self.cookie_file_path)

handle_cookie = handle_cookie()

if __name__ == '__main__':
    aaa ={'aliyungf_tc': 'AQAAALDn9HZUWg4A0zVYZQqrwUo7zYO6'}
    handle_cookie.write_cookie(aaa,"app")