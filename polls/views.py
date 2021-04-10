from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from nlp_chat_robot.main import *
import json

# from mysite.api.nlp_chat_robot.main import get_response

# from dwebsocket.decorators import accept_websocket
# from nlp_chat_robot.main import get_response

# def http_request(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         print(data["msg"])
#         resp = get_response(data["msg"])
#     else:
#         resp = {'errorcode': 100, 'record': 'Get success'}
#     return HttpResponse(json.dumps(resp), content_type="application/json")


# @accept_websocket
# def index(request):
#     if request.is_websocket():
#         print('websocket connection....')
#         msg = request.websocket.wait()
#         print(msg, type(msg), json.loads(msg))
#         while 1:
#             if msg:
#                 for i in range(10):
#                     request.websocket.send('service message: {}'.format(i).encode())  # 向客户端发送数据
#                     time.sleep(0.5)  # 每0.5秒发一次
#                 request.websocket.close()
#     else:
#         httpRequest(request)

def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["msg"])
        resp = get_response(data["msg"])
        # resp=get_response(data["msg"])
    else:
        resp = {'errorcode': 100, 'record': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")