#-*- coding: UTF-8 -*-
import json
from utlis.read_res.ReadExec import Read_exec
from utlis.read_res.ReadIni import read_ini
from utlis.read_res.GetKeyValue import GetKeyValue
from common.BaseRequest import base_request
import ddt
import unittest
data = Read_exec(file_name="bd").get_all_lines()
bd_host = read_ini.get_content("server","bd_host")
@ddt.ddt
class TestBaiDu(unittest.TestCase):


  @ddt.data(*data)
  def test_sugrec(self,data):
        test_id,role,is_perform,condition,url,method,data_json,cookie,header,check_field,check_value,result=data
        if is_perform=="yes":
            res =base_request.send_request(method,url=bd_host+url,data=json.loads(data_json))
            data_list =GetKeyValue(res.text).search_key(check_field)
            for i in data_list:
                txt = i.lower()
                if check_value not in txt:
                    self.assertFalse("不存在:"+"实际结果:"+check_value+"  失败结果:"+i)
            res.close()


if __name__ == '__main__':
    unittest.main()
