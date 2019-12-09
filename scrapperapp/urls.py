from django.urls import path
from scrapperapp.views import *

urlpatterns = [

    path('index/', index),
    path('home/', home),

]
