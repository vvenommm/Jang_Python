from django.http import HttpResponse
from django.shortcuts import render
from HELLO_DJ_MEM.memdao import MemDao

def index(request):
    return HttpResponse("Hello, EMP")

def mem_list(request):
    mem = MemDao()
    list = mem.memSelects()
    return render(request, 'mem_list.html', {'list' : list})

def mem_detail(request):
    m_id = request.GET.get('m_id', None)
    mem = MemDao()
    mem = mem.memSelect(m_id);
    return render(request, 'mem_detail.html', {'mem' : mem})

def mem_mod(request):
    m_id = request.GET.get('m_id', None)
    return render(request, 'mem_mod.html', {'m_id' : m_id})

def mem_mod_act(request):
    if request.method == "POST":
        m_id = request.POST.get('m_id', '')
        m_name = request.POST.get('m_name', '')
        m_tel = request.POST.get('m_tel', '')
        m_addr = request.POST.get('m_addr', '')
        
        mem = MemDao()
        cnt = mem.memUpdate(m_id, m_name, m_tel, m_addr)
        return render(request, 'mem_mod_act.html', {'cnt' : cnt})
    
def mem_del(request):
    m_id = request.GET.get('m_id', None)
    mem = MemDao()
    cnt = mem.memDelete(m_id)
    return render(request, 'mem_del.html', {'cnt' : cnt})

def mem_ins(request):
    return render(request, 'mem_ins.html')

def mem_ins_act(request):
    if request.method == "POST":
        m_name = request.POST['m_name']
        m_tel = request.POST['m_tel']
        m_addr = request.POST['m_addr']
        
        mem = MemDao()
        cnt = mem.memInsert( m_name, m_tel, m_addr)
        return render(request, 'mem_ins_act.html', {'cnt' : cnt})
