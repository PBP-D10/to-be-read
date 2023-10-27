from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('book:Home'))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    return render(request, "login.html")

def register_view(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your account has been successfully created!')
            return HttpResponseRedirect(reverse('Login'))
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='Login')
def logout_view(request):
    logout(request)
    response = HttpResponseRedirect(reverse('Login'))
    return response