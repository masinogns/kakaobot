from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학식', '정문', '후문']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
            'message': {
                'text': today_date + '의 ' + cafeteria_name + ' 중식 메뉴입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['처음으로', '뒤로가기']
            }

        })
