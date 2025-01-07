from django.urls import path
from . import views

app_name = 'phoneapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('send/', views.send, name='send'),
    path('about/', views.about, name='about'),
    path('comminecation/', views.comminecation, name='comminecation'),
    path('basket/', views.basket, name="basket"),
    path('computer/', views.computer, name="computer"),
    path('tablet/',views.tablet, name='tablet'),
    path('earphones/',views.earphones, name='earphones'),
    path('newrealeses/',views.newrealeses, name='newrealeses')
]
