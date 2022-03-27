from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from bot import line_message

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        print("req:",request)
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        data = request['events'][0]
        print("data:",data)
        line_message.reply(data, signature)
        return HttpResponse("OK")
    return HttpResponse("Other Post..")

@csrf_exempt
def blank(request):
    print(request.method)
    return HttpResponse("Hello World!")
