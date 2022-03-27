from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from bot.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        print("req:",request)
        signature = request.headers['X-Line-Signature']
        data = request['events'][0]
        print("data:",data)
        LineMessage.reply(data, signature)
        return HttpResponse("OK")
    return HttpResponse("Other Post..")

@csrf_exempt
def blank(request):
    print(request.method)
    return HttpResponse("Hello World!")
