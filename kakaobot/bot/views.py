from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):

    return JsonResponse(
    {
    "type" : "buttons",
    "buttons" : [u"오늘의 메뉴", u"내일의 메뉴", u"이번주 메뉴"]
    }
    )

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']

    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse(
    {
        {
            "message":{
                "text" : "제대로 알려주세요!\n어떤 맛있는 메뉴가 기다리고 있을까요?"
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : [
                    u"오늘의 메뉴",
                    u"내일의 메뉴",
                    u"이번주 메뉴"
                ]
            }
        },
        {
            "message":{
                "text" : "=오늘의 메뉴=\n밥\n된장국\n돈까스\n뾰로롱"
            } # keyboard는 모든 메세지에 붙어있다. 코드 길이상 생략했다.
        },
        {
            "message":{
                "text" : "=내일의 메뉴=\n연어덮밥\n먹고싶다\n돈까스도\n먹고싶다"
            }
        }
    }

    )
