from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#password for test user Ashish$$$12345

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'index.html')


def loginUser(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def signupUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'signup.html', {'form':form})
        