from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def R15(request):
    return HttpResponse(''' <h1> R15 MODEL V3</h1>
                            <h1> R15 PRICE 💵250000</h1>
                            <h1> R15 SPEED 180KMPH</h1>
                            <img src="https://5.imimg.com/data5/UC/AP/MY-989864/gray-color.png"</img>
                        ''')

