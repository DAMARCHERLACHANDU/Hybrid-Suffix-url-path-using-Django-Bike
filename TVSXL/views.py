from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TVSXL(request):
    return HttpResponse(''' <h1> TVSXL MODEL </h1>
                            <h1> TVSXL PRICE 💵50000</h1>
                            <h1> TVSXL SPEED 100KMPH</h1>
                            <img src="https://www.tvsmotor.com/tvs-xl100/-/media/Brand-Pages/XL100/Features-Heavy-DutyKS/Style/optimized-images/Bold-Styling.png"</img>
                            
                        ''')