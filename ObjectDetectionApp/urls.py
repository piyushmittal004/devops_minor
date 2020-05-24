from django.urls import path
from . import views

urlpatterns = [
    path('', views.launch, name='home-page'),
    path('runCode', views.objectDetectionAlgo, name='runCode'),
    path('result', views.result, name='result'),
    path('getCode', views.getCode, name='getCode'),
]