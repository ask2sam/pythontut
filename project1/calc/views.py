from sqlalchemy import create_engine
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Index page")

def htmlpage(request):
    return render(request, 'index.html', {'name' : 'Shamshad'})

def home(request):    
    engine = create_engine('mysql+pymysql://root:@localhost:3306/php_oop_crud_level_1')
    # alltables = engine.table_names()
    v = engine.execute("select * from products")
    arr = []
    for i in v:
        arr.append(i)
    return HttpResponse(arr)

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, 'result.html', {'result' : res})
