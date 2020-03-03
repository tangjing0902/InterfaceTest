# -*- coding: UTF-8 -*-
import time
import xlrd
from utlis.file.FileUtil import file_utils

class Read_exec(object):
    file_path = "config/data.xlsx"

    def __init__(self,file_name=None,index=0):
        self.data = xlrd.open_workbook(file_utils.location_file(self.file_path),encoding_override="utf-8")
        if file_name:
            self.table = self.data.sheet_by_name(file_name)
        else:
            self.table = self.data.sheet_by_index(index)

    #返回表的实例
    def get_table(self):
        return self.table


    #返回表中所有行的数据
    def get_all_lines(self):
        data =[]
        for i in range(self.table.nrows):
            if i>0:
                data.append(self.table.row_values(i))
        return data



    #根据列名称获取行的数据
    def get_specified(self,col_name,col_index=0):
        clo_index = self.table.col_values(col_index).index(col_name)
        return self.get_all_lines()[clo_index-1]



    def __get_columns(self):
        data =[]
        for i in range(self.table.ncols):
            data.append(self.table.col_value(i))
        return data

