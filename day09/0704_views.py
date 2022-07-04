from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, Django")

def para(request):
    a = request.GET.get('a', None)
    return HttpResponse("Hello, para" + a)

def post(request):
    if request.method == "POST":
        a = request.POST['a']
        '''data = {
            'numbers' : a
            }'''
    return HttpResponse("Hello, POST<br>request로 넘어온 파라미터 : {}".format(a))
    # return render(request, 'post.html', data)

def forward(request):
    a= "후후리"
    b=["후후리", "1조", "PL입니다."]
    c=[
        {'e_id' : '1', 'e_name' : 'David', 'sex' : 'F', 'addr' : 'fgeh'},
        {'e_id' : '2', 'e_name' : 'John', 'sex' : 'M', 'addr' : 'abcde'}
        ]
    # return render(request, 'forward.html', {'name' : a,})
    return render(request, 'forward.html', {'a' : a, 'b' : b, 'c' : c})
