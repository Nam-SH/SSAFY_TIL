# django import style guide
# 1. standard library
# 2. third-pardy (request ...)
# 3. Django
# 4. local django


import random
from datetime import datetime
from pprint import pprint
import requests
from django.shortcuts import render

# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()의 첫 번재 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버걸', '취킨', '김밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


def image(request):
    return render(request, 'pages/image.html')


def hello(request, name):
    menu = ['족발', '햄버걸', '취킨', '김밥']
    pick = random.choice(menu)
    context = {'pick': pick, 'name': name,}
    return render(request, 'pages/hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3, 'num1': num1, 'num2': num2,}
    return render(request, 'pages/times.html', context)


def template_language(request):
    menus = ['자장면', '탕수육', '라조기', '양장피', '찜뽕',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
      'menus': menus,
      'my_sentence': my_sentence,
      'messages': messages,
      'empty_list': empty_list,
      'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'pages/isitgwangbok.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    pprint(request.META)
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    # 3. str 을 리스트로 바꿔서 저장
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}

    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')