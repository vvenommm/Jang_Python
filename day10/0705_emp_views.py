from django.http import HttpResponse
from django.shortcuts import render
from HELLO_DJ_EMP.empdao import EmpDao
from gevent.libev.corecext import NONE

def index(request):
    return HttpResponse("Hello, EMP")

def emp_list(request):
    ed = EmpDao()
    list = ed.myselects()
    return render(request, 'emp_list.html', {'list' : list})

def emp_detail(request):
    e_id = request.GET.get('e_id', None)
    ed = EmpDao()
    emp = ed.selectone(e_id)
    return render(request, 'emp_detail.html', {'emp' : emp})

def emp_mod(request):
    e_id = request.GET.get('e_id', None)
    # ed = EmpDao()
    # emp = ed.selectone(e_id)
    return render(request, 'emp_mod.html', {'e_id' : e_id})

def emp_mod_act(request):
    if request.method == "POST":
        e_id = request.POST.get('e_id', '')
        e_name = request.POST.get('e_name', '')
        sex = request.POST.get('sex', '')
        addr = request.POST.get('addr', '')
        
        ed = EmpDao()
        cnt = ed.myupdate(e_name, addr, e_id)
        return render(request, 'emp_mod_act.html', {'cnt' : cnt})
    
def emp_del(request):
    e_id = request.GET.get('e_id', None)
    ed = EmpDao()
    cnt = ed.mydelete(e_id)
    return render(request, 'emp_del.html', {'cnt' : cnt})

def emp_ins(request):
    return render(request, 'emp_ins.html')

def emp_ins_act(request):
    if request.method == "POST":
        e_name = request.POST['e_name']
        sex = request.POST['sex']
        addr = request.POST['addr']
        
        ed = EmpDao()
        cnt = ed.myinsert( e_name, sex, addr)
        return render(request, 'emp_ins_act.html', {'cnt' : cnt})
