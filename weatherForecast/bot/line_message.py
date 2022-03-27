from django.http import HttpResponse
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)

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
    print("text=",event.message.text)
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