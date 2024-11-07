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
    path('useradv_chat/<pk>',views.useradv_chat,name='useradv_chat'),
    # path('user_sendmsg/<pk>',views.user_sendmsg),


    #Advocate_reg
    path('Adv_reg',views.Adv_reg),

    #Advocate_log
    path('Adv_log',views.Adv_log),
    path('Adv_logout',views.Adv_logout),

    #Advocate
    path('Adv_index',views.Adv_index),
    path('Adv_reg_form',views.Adv_reg_form),
    path('Adv_profile',views.Adv_profile),
    path('advprof_Activate',views.advprof_Activate),
    path('advprof_Deactivate',views.advprof_Deactivate),
    path('Update_prof',views.Update_prof),
    path('adv_msg',views.adv_msg),
    path('advuser_chat/<pk>',views.advuser_chat,name='advuser_chat'),
    path('adv_clients',views.adv_clients),
]