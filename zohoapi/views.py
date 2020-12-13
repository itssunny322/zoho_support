from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect,reverse
import requests
from .forms import *
import json



# Create your views here.
def index(request):
    return render(request, 'index.html', {'title':'index'})

def logout(request):
    return render(request, 'logout.html', {'title':'logout'})

def register(request):
    return render(request, 'register.html', {'title':'register'})

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})

def ticket_add(request):

    ticket_form = TicketPostForm(request.POST or None)
    url = 'https://desk.zoho.com/api/v1/tickets'
    url_token = 'https://accounts.zoho.com/apiauthtoken/nb/create'
    data_for_token = '?SCOPE=ZohoSupport/supportapi,ZohoSearch/SearchAPI&EMAIL_ID=dauntless2310@gmail.com&PASSWORD=bruno@321'
    token = requests.post(url_token, data=data_for_token)


    if request.method == 'POST' and ticket_form.is_valid():
        data = {
            "department": ticket_form.cleaned_data['department'],
            "category": ticket_form.cleaned_data['category'],
            "subject": ticket_form.cleaned_data['subject'],
            "description": ticket_form.cleaned_data['description'],
            "priority": ticket_form.cleaned_data['description']
        }

        x = requests.post(url, data=data,headers={'Authorization':token.AUTHTOKEN })
        messages.success(request,'Ticked added successfully')
        return render(request, 'index.html', {'title':'index'})
    context = {'ticket_form': ticket_form}
    return render (request,'add.html',context)


def ticket_list(request):

    url = 'https://desk.zoho.com/api/v1/tickets'
    url_token = 'https://accounts.zoho.com/apiauthtoken/nb/create'
    data_for_token = '?SCOPE=ZohoSupport/supportapi,ZohoSearch/SearchAPI&EMAIL_ID=dauntless2310@gmail.com&PASSWORD=bruno@321'
    token = requests.post(url_token, data=data_for_token)
    list = requests.get(url,headers={'Authorization':token.AUTHTOKEN })

    ticket_list=list.data

    return render(request, 'list.html', {'ticket_list': 'ticket_list'})

