from bot import line_message
import unittest
from django.test import TestCase
import os
import sys
import pprint

sys.path.append(os.path.abspath("bot"))
pprint.pprint(sys.path)

# sut = line_message()


class TestLine_message(TestCase):
    def test_handleLocale(self):
        event = {
            # "headers": {
            #     "x-line-signature": "dummy"
            # },
            # "body": '{"events":[{"type":"location","message":{"latitude":"35","longitude":"139"},"replyToken":"dummy"}]}'
            # "message": '{"events":[{"type":"location","message":{"latitude":"35","longitude":"139"},"replyToken":"dummy"}]}'
            "message": "aaa"
            # "message": {
            #     "type": "location",
            #     "title": "my location",
            #     "address": "Tokyo",
            #     "latitude": 35.65910807942215,
            #     "longitude": 139.70372892916203
            # }
        }
        line_message.handleLocale(event)
        print("Sucess!!")
