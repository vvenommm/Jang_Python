from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from HELLO_AX_EMP.empdao import EmpDao

def emp_list(request):
    return render(request, 'emp_list.html')

def emp_list_axios(request):
    
    em = EmpDao()
    list = em.myselects();
    # e_id = request.GET.get('e_id', '')
    # print("e_id", e_id)
    context = {
        'list': list
        }
    return JsonResponse(context)

def emp_detail_axios(request):
    e_id = request.GET.get('e_id', '');
    # if request.method == "POST":
    #     e_id = request.POST['e_id']
    
    em = EmpDao()
    emp = em.selectone(e_id)
    context = {
        'emp' : emp
        }
    return JsonResponse(context)

def emp_upd_axios(request):
    e_id = request.GET.get('e_id', '');
    e_name = request.GET.get('e_name', '');
    addr = request.GET.get('addr', '');
    # if request.method == "POST":
    #     e_id = request.POST['e_id']
    #     e_name = request.POST['e_name']
    #     addr = request.POST['addr']
    #
    #     em = EmpDao()
    #     cnt = em.myupdate(e_id, e_name, addr)
    em = EmpDao()
    cnt = em.myupdate(e_id, e_name, addr)
    print(cnt)
        
    context = {
        'cnt' : cnt
        }
    return JsonResponse(context)

def emp_add_axios(request):
    if request.method == "POST":
        e_name = request.POST['e_name']
        sex = request.POST['sex']
        addr = request.POST['addr']
        # sex = request.POST.get('sex')
        # addr = request.POST.get('addr')
        
        print(e_name)
        
    em = EmpDao()
    cnt = em.myinsert(e_name, sex, addr)
    
    context = {
        'cnt' : cnt
        }
    return JsonResponse(context)

def emp_del_axios(request):
    if request.method == "POST":
        e_id = request.POST['e_id']
        
    em = EmpDao()
    cnt = em.mydelete(e_id);
    
    context = {
        'cnt' : cnt
        }
    return JsonResponse(context)
