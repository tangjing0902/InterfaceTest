#-*- coding: UTF-8 -*-
import json
from utlis.read_res.ReadExec import Read_exec
from utlis.read_res.ReadIni import read_ini
from utlis.read_res.GetKeyValue import GetKeyValue

from common.BaseRequest import base_request
from utlis.handle_results import handle_results
import ddt
import unittest
import ast
data = Read_exec(file_name="慕课网").get_all_lines()
imooc_host = read_ini.get_content("server","imooc_host")

@ddt.ddt
class TestImooc(unittest.TestCase):


  @ddt.data(*data)
  def test_sugrec(self,data):
        test_id,role,is_perform,condition,url,method,data_json,cookie,header,check_field,check_value=data
        if is_perform=="yes":
                res =base_request.send_request(method,url=imooc_host+url,data=json.loads(data_json))
                print(res.text)
                cf_list = handle_results.get_ec_field(check_field)
                cv_list = handle_results.get_ec_field(check_value)
                for i in range(len(cf_list)):
                    data_list = GetKeyValue(res.text).search_key(cf_list[i])
                    for  h_data in data_list:
                        self.assertEqual(str(h_data),cv_list[i])

                #     if fd == 'json':
                #         print('我是json')
                #         pass
                #     else:
                #         print(fd)


                #
                # print(data_list)
            # for i in data_list:
            #     print(check_value)
            #     if check_value not in i:
            #         print("查询字段："+check_field)
            #         print("预期值："+check_value)
            #         print("实际值："+i)
            #         self.assertFalse("不存在:"+"实际结果:"+check_value+"  失败结果:"+i)
        #     res.close()
if __name__ == '__main__':
    unittest.main()
