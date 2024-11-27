from django.urls import path
from KTM.views import *

urlpatterns = [
    path('model/',model,name='model'),
    path('price/',price,name='price'),
    path('speed/',speed,name='speed'),
]
