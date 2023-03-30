from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# view.py의 함수에 들어있는 request 파라미터 : 요청 객체
def index(request):
    template = loader.get_template('app/index.html')

    # dictionary 타입의 변수 context
    context = {}

    # 응답객체안에 템플릿과 표시할 값(context), 요청(request)
    return HttpResponse(template.render(context, request))


def call1(request):
    template = loader.get_template('app/template.html')
    print(request)  

    context = {}

    return HttpResponse(template.render(context, request))


# RESTful 방식으로 호출된 주소에 대한 함수
# 요청 객체 뒤의 파라미터에 해당하는 변수명 써줘야함
def call2(request, number):
    # 파이썬에서는 자료형이 다른 것을 합칠 수 없음
    # print('number:', number)   >> 불가
    print("number:", number)

    template = loader.get_template('app/template.html')

    context = {}

    return HttpResponse(template.render(context, request))


def call3(request):
    # request 객체에서 가져오는 모든 데이터는 str 타입
    name = request.GET['name']
    age = request.GET['age']

    print('name:', name)
    print(type(age))

    return HttpResponse('호출됨')


def call4(request):
    template = loader.get_template("app/template.html")

    context = {
        # 문자열 하나 보내기
        'item':'This text is sent from server.',
        'name':'박승인',
        # 리스트 보내기
        'board_list':[
            {'title':'1등', 'writer':'홍길동'},
            {'title':'2등', 'writer':'홍길동'},
            {'title':'3등', 'writer':'홍길동'},
        ],
        # 딕셔너리 보내기   
        'mydata':{
            'name':'박승인',
            'age':'24',
            'address':'광주'
        }
    }

    return HttpResponse(template.render(context, request))


def call5(request):
    template = loader.get_template("app/tag.html")

    language = ['kor', 'eng', 'jap', 'chi']

    context = {
        'list': language,
        'number': -3
    }

    return HttpResponse(template.render(context, request))


def call6(request):
    template = loader.get_template('app/form.html')

    context = {}

    return HttpResponse(template.render(context, request))


def call_submit(request):

    name = request.POST['name']
    age = request.POST['age']

    print('name:', name)
    print('age:', age)
    
    return HttpResponse('submit OK')


def call7(request):

    template = loader.get_template('app/template.html')

    context = {
        'name':'박승인',
        'age': 24,
        'address':'화순',
    }

    return HttpResponse(template.render(context, request))