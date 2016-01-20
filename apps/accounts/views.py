
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from .decorators import anonymous_required
from .forms import RegistrationForm, LoginForm
from .models import Account


@anonymous_required('index')
def login_user(request, login_success_url="/", template="accounts/login.html"):
    """ 
    	Login view 
    """
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        form = LoginForm(request.POST)
        if user is not None:
            login(request, user)
            return redirect(login_success_url)
    else:
        form = LoginForm()
    
    return render(request, template, {'form': form})


@anonymous_required('index')
def register_user(request, register_success_url="/", template="accounts/register.html"):
    """
    	Registration view
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = Account.objects.create_user(
                username=username,
                email=email,
                password=password)

            user.save()

            subject = "Welcome"

            recipients = [email,]

            auth_usr = authenticate(username=username,
                                    password=password)

            if auth_usr:
                login(request, auth_usr)
            
            return redirect(register_success_url)
    else:
        form = RegistrationForm()
    
    return render(request, template, {'form': form})





