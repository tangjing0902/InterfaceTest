# -*- coding: UTF-8 -*-
import os
class FileUtil(object):


    '''
     定位到项目中文件路径 从项目根目录开始 
     '''
    def location_file(self,file_name):
        file_path =None
        path = os.path.split(os.path.realpath(__file__))[0]  # 定位类目录
        file_path = os.path.abspath(os.path.join(path, "..","..", file_name))  # 定位到项目根目录
        if os.path.exists(file_path):
            return file_path
        else:
            print ("此路径不存在："+file_path)
        return file_path


    '''
     定位到项目中文件路径 从项目根目录开始 
     '''
    def write_file(self,file_path,msg,isRepeat=False):
        wr_file = open(file_path,mode="a",encoding="utf-8")
        if not isRepeat :
            re_file = open(file_path, mode="r",encoding="utf-8").readlines()
            with wr_file as f:
                if msg not  in re_file:
                    f.write(msg)
        else:
            with wr_file as f:
                f.write(msg)
        f.close()

    def read_file(self,file_path):
        return open(file_path, mode="r", encoding="utf-8").readlines()

file_utils = FileUtil()
if __name__ == '__main__':
    x=0
    for i in range(10000000000000):
        file_utils.write_file("D:\Test\资料\Linux与shell\\test.txt","123456"+str(x)+"\n")
        x=x+1

