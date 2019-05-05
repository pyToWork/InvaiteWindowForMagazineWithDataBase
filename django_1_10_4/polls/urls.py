from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index1),#сылка на первую тест страницу и функция 1 
    url(r'',views.index2),# cылка на вторую тест страницу и функция 2
]