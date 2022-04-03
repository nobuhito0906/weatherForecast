from django.test import TestCase
import os
import sys
from bot import open_meteo
import pprint

# sys.path.append(os.path.abspath("bot"))

# pprint.pprint(sys.path)
class Test_open_meteo(TestCase):
    
    # sut = Open_meteo()
    def test_reqSdk(self):
        latitude = 35.96943871442791
        longitude = 139.73454069496742
        open_meteo.Open_meteo.reqSdk(self,latitude,longitude)
