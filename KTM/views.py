from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def model(request):
    return HttpResponse('''<h1> KTM MODEL 390 </h1>
                           <img src="https://static.autox.com/uploads/2022/10/KTM-RC-200-Dark-Galvano.jpg"></img>
                        ''')

def price(request):
    return HttpResponse('<h1>KTM 390 PRICE 💵200000</h1>')

def speed(request):
    return HttpResponse('<h1>KTM 390 PRICE 120KMPH</h1>')