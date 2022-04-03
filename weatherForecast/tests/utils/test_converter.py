from django.test import TestCase
from bot.utils import converter
import os
import sys
import pprint

sys.path.append(os.path.abspath("utils"))
pprint.pprint(sys.path)

class Test_converter(TestCase):
    def test_weatherCode(self):
        code = converter.Converter.weatherCode(self,0)
        print("code:",code)
        self.assertEqual(code,"快晴だよ!!")
        
    def test_none_code(self):
        code = converter.Converter.weatherCode(self,111)
        print("code:",code)
        self.assertEqual(code,"そんなコードないよ")
        