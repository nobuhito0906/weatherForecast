from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from bot import line_message

@csrf_exempt
def index(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        print("body:",body)
        line_message.reply(body, signature)
        return HttpResponse("OK")
    return HttpResponse("Other Post..")

@csrf_exempt
def blank(request):
    print(request.method)
    return HttpResponse("Hello World!")
