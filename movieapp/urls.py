from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('upcoming/',views.upcoming,name='upcoming'),
    path('updetails/<str:pk>/',views.updetails,name='updetails'),
    path('about/',views.about,name='about'),
    path('details/<str:pk>/',views.detailsmovie,name='details-movie'),
    path('signup/',views.signup,name='signup'),
    path('booked/',views.booked,name='booked'),
    path('login/',views.login,name='login'),
]
