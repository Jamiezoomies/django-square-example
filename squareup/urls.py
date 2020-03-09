from django.urls import path

from . import views

app_name = 'sqaureup'
urlpatterns = [
    path('', views.index, name='index'),
    path('process-payment', views.payment, name='payment'),
]