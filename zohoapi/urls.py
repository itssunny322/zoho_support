from django.urls import path

from .views import *

urlpatterns =[
    path('', Login, name ='login'),
    path('index', index, name = 'index'),
    path('register', register, name = 'register'),
    path('logout', logout, name = 'logout'),
    path('ticket_add', ticket_add, name='ticket_add'),
    path('ticket_list',ticket_list, name='ticket_list')
]