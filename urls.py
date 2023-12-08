from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.gym, name='gym'),
    path('index/submit', views.sum , name='submit'),
    path('show/', views.show , name = 'show')
]
