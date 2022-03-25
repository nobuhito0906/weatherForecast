from distutils.log import error
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
import os

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESS_TOKEN
}


class LineMessage():
    def __init__(self, messages, req_url):
        self.messages = messages
        self.req_url = req_url
    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        if not self.req_url:
            print("位置情報送るよ")
            REPLY_ENDPOINT_URL = self.req_url
        req = urllib.request.Request(
            REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)
