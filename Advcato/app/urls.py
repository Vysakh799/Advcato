from django.urls import path
from . import views
urlpatterns = [
    #index Page
    path('',views.index),

    #Login Page
    path('login',views.login),

    #about Page
    path('about',views.about),

    #contact Page
    path('contact',views.contact),

    #User_reg
    path('Ureg',views.Ureg),

    #User_log
    path('Ulog',views.Ulog),

    #User
    path('User_index',views.User_index),
    path('User_logout',views.User_logout),


    #Advocate_reg
    path('Adv_reg',views.Adv_reg),
]