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
    path('Advocates',views.Advocates),
    path('advuser_profile/<pk>',views.advuser_profile),
    path('user_msg',views.user_msg),
    path('useradv_chat',views.useradv_chat),


    #Advocate_reg
    path('Adv_reg',views.Adv_reg),

    #Advocate_log
    path('Adv_log',views.Adv_log),

    #Advocate
    path('Adv_index',views.Adv_index),
    path('Adv_reg_form',views.Adv_reg_form),
    path('Adv_profile',views.Adv_profile),
    path('advprof_Activate',views.advprof_Activate),
    path('advprof_Deactivate',views.advprof_Deactivate),
    path('Update_prof',views.Update_prof),
    path('advuser_chat',views.advuser_chat),
]