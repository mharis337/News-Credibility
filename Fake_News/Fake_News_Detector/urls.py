from django.urls import path
from Fake_News_Detector import views

urlpatterns= [
    path(r'', views.index, name='index'),

]