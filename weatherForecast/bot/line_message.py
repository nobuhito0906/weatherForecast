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
from openmeteo_py import Hourly, Daily, Options, OWmanager, timezones

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
if ACCESS_TOKEN != "":
    print("is AccessToken")
else:
    print("not Token")
SECRET = os.getenv("CHANNEL_SECRET")

line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
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
        hourly = Hourly()
        daily = Daily()
        daily.temperature_2m_max()
        daily.temperature_2m_min()
        daily.apparent_temperature_max()
        daily.apparent_temperature_min()
        tmz = timezones.Tokyo
        options = Options(latitude, longitude,
                          current_weather="true", timezone=tmz)

        mgr = OWmanager(options,hourly.all(),
                        daily.all())
        print("open-meteo SDK")
        data = mgr.get_data()
        currentWeather = data['current_weather']
        temperature = currentWeather['temperature']
        windSpeed = currentWeather['windspeed']
        weatherCode = currentWeather['weathercode']
        print("currentWeather:",currentWeather)
        print("weathercode:",weatherCode)
        print("temperature:",temperature)
        print("windSpeed:",windSpeed)
        currentText = f"現在の天気:{0} 気温:{1} 風速:{2}".format(weatherCode,temperature,windSpeed)
        print("daliy MaxTempature:",data['daily']['temperature_2m_max'][0])
        print("daily Min Tempature:",data['daily']['temperature_2m_min'][0])
        message = "緯度:{}\n経度:{}".format(latitude, longitude)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message),
            TextSendMessage(currentText)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="どこそれ")
        )
