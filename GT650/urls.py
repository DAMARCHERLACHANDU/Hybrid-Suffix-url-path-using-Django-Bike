from django.urls import path

from GT650.views import *

urlpatterns = [
    path('model/',model,name='model'),
    path('price/',price,name='price'),
    path('speed/',speed,name='speed'),
]
