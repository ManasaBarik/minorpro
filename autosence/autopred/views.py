from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # redirect to dashboard page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # creates the user
            login(request, user)        # auto-login after register (optional)
            messages.success(request, "Registration successful. Welcome!")
            return redirect("dashboard")    # change target as you like
        else:
            # debug helper — will show form errors in the console where runserver is running
            print("REGISTER FORM ERRORS:", form.errors.as_json())
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})
# @login_required
def dashboard_view(request):
    return render(request, "dashboard.html")