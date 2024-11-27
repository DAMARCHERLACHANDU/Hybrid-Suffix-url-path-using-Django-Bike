from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def model(request):
    return HttpResponse('''<h1>ROYAL ENFIELD GT650</h1>
                        
                            <img src="https://cdn.bikedekho.com/processedimages/royal-enfield/continental-gt-650/source/continental-gt-65064155f76ab11f.jpg"</img>
                        ''')
    

def price(request):
    return HttpResponse('''<h1>ROYAL ENFIELD GT650 PRICE 💵400,000</h1>
                        
                            <img src="https://cdn.bikedekho.com/processedimages/royal-enfield/continental-gt-650/source/continental-gt-65064155f76ab11f.jpg"</img>
                        ''')

def speed(request):
    return HttpResponse('''
                            <h1>ROYAL ENFIELD GT650 SPEED 150KMPH 🏍️</h1>
                            
                        ''')
    
