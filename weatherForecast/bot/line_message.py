import json
from django.http import HttpResponse
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
import datetime

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
        # 現在時刻
        dt_now = datetime.datetime.now()
        print("NOW:",dt_now)
        # Open-Meteoの天気予報API
        opmtResponse = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly={}".format(
            latitude, longitude, dt_now.hour)
        print("opmtResponse:", opmtResponse)
        message = "緯度:{}\n経度:{}".format(latitude, longitude)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message),
            TextSendMessage(opmtResponse.json())
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="どこそれ")
        )
