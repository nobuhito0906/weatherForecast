from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from bot.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token=data['replyToken']
        if message['text'] == '現在地':
            line_message=LineMessage("https://line.me/R/nv/location/")    
        else:
            line_message=LineMessage(message_creater.create_single_text_message(message['text']))
        
        line_message.reply(reply_token)
        return HttpResponse("OK")
    return HttpResponse("Other Post..")

@csrf_exempt
def blank(request):
    print(request.method)
    return HttpResponse("Hello World!")
