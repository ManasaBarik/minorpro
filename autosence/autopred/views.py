from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def details(request):
    return render(request, 'details.html')  # if you make a details.html

def predict(request):
    if request.method == "POST":
        # later handle ML model prediction here
        pass
    return render(request, 'predict.html')

def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")
