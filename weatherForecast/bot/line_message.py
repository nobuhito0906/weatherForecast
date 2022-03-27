import json
from django.http import HttpResponse
import datetime
import requests
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage
)
from linebot.exceptions import (
    InvalidSignatureError
)
from openmeteo_py import Hourly, Daily, Options, OWmanager, timezones

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
SECRET = os.getenv("CHANNEL_SECRET")

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)


def reply(data, signature):
    try:
        handler.handle(data, signature)
    except InvalidSignatureError:
        return HttpResponse("Sigature Error..")
    return HttpResponse("OK")


@handler.add(MessageEvent, message=TextMessage)
def handleMessage(event):
    if event.message.text == '現在地':
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="位置情報送るよ"),
                TextSendMessage(text="https://line.me/R/nv/location/")
            ]
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )


@handler.add(MessageEvent, message=LocationMessage)
def handleLocale(event):
    print("type:", event.message.type)
    if event.message.type == "location":
        latitude = event.message.latitude
        longitude = event.message.longitude
        # Open-Meteo SDKを利用
        hourly =Hourly()
        # daily = Daily()
        tmz = timezones.Tokyo
        options = Options(latitude, longitude, timezone=tmz)
        
        mgr = OWmanager(options,
            hourly.all(),
            # daily.all()
            )
        print("open-meteo SDK")
        meteo = mgr.get_data()
        print("meteo:", meteo)
        message = "緯度:{}\n経度:{}".format(latitude, longitude)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message),
            TextSendMessage(meteo)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="どこそれ")
        )
