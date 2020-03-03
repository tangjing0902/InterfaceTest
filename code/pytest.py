#-*- coding: UTF-8 -*-
import pytest



class TestClass:

     def setup_class(self):
        print("setup_class")

     @pytest.mark.slow
     def test1(self):
         name ="yes"
         assert name=="no"
     @pytest.mark.slow
     def test2(self):
        print("3456")

if __name__ == '__main__':
    pytest.main()