# -*- coding: UTF-8 -*-
from jsonpath_rw import parser
import re
class handle_results(object):


    #预期检查字段切割
    def get_ec_field(self,name):
        field_lists = []
        if name!=None and '$'in name:
            return list(filter(None,name.split('$')))
        field_lists.append(name)
        return field_lists


    def depend_data(self,data):
        data_list = data.split(">")
        return data_list





handle_results = handle_results()

