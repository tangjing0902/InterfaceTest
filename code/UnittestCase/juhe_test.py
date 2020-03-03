#-*- coding: UTF-8 -*-
import json
import ddt
import unittest
from utlis.read_res.ReadExec import Read_exec
from utlis.read_res.ReadIni import read_ini
from utlis.read_res.GetKeyValue import GetKeyValue
from utlis.handlle_json import handle_json
from utlis.handle_results import handle_results
from utlis.handlle_json import handle_json
from utlis.handle_cookie import handle_cookie
from common.BaseRequest import base_request


data = Read_exec(file_name="聚合").get_all_lines()
imooc_host = read_ini.get_content("server","juhe_host")

@ddt.ddt
class TestImooc(unittest.TestCase):


  @ddt.data(*data)
  def test_sugrec(self,data):
        cookie=None
        get_cookie=None
        headers=None
        test_id,environment,role,is_perform,condition,url,method,data_json,cookie_perform,header_perform,check_field,check_value=data
        if is_perform=="yes":
            if cookie_perform == "yes":
                cookie = handle_cookie.get_cookie_value(environment)
            elif cookie_perform== "write":
                get_cookie = {"is_cookie":environment}
            if header_perform=="yes":
                headers = handle_json.get_data_value("config/header.json",environment)
            res =base_request.send_request(method,imooc_host+url,json.loads(data_json),cookie=cookie,get_cookie=get_cookie,header=headers)

            print("res=============>",res)
            cf_list = handle_results.get_ec_field(check_field)
            cv_list = handle_results.get_ec_field(check_value)
            for i in range(len(cf_list)):
                if cf_list[i]=='json':
                    load_data = handle_json.read_json("config/user_data.json").get(url)
                    json_check_results= handle_json.check_json_format(load_data,json.loads(res))
                    self.assertTrue(json_check_results)
                else:
                    data_list = GetKeyValue(res).search_key(cf_list[i])
                    self.assertTrue(data_list !=[] and data_list!=None,"字段{0}不存在json中".format(cf_list[i]))
                    for h_data in data_list:
                        print(cv_list[i])
                        print(str(h_data))
                        self.assertEqual(str(h_data), cv_list[i])




if __name__ == '__main__':


    unittest.main()
