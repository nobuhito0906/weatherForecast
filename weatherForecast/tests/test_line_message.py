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
            "message": {
                "address": "\u65e5\u672c\u3001\u3012344-0048 \u57fc\u7389\u770c\u6625\u65e5\u90e8\u5e02\u5357\u4e2d\u66fd\u6839\uff16\uff18\uff13\u2212\uff18",
                "id": "15849613441582",
                "latitude": 35.96943871442791,
                "longitude": 139.73454069496742,
                "type": "location"
            },
            "mode": "active",
            "replyToken": "58caad25cd194966a4bcb4eb03094b76",
            "source": {
                "type": "user",
                "userId": "U5ee46365ccf772bdddd1c4a5571a8e4b"
            },
            "timestamp": 1648886091311,
            "type": "message"
            }
            # "headers": {
            #     "x-line-signature": "dummy"
            # },
            # "body": '{"events":[{"type":"location","message":{"latitude":"35","longitude":"139"},"replyToken":"dummy"}]}'
            # "message": '{"events":[{"type":"location","message":{"latitude":"35","longitude":"139"},"replyToken":"dummy"}]}'
        
        line_message.handleLocale(event)
        print("Sucess!!")
