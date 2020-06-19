from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from rest.apps.main.models import Restorant
from .forms import RestourantForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def log(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return redirect("index")



def auth(request):
    form = UserCreationForm(request.POST)
    i = 1
    try:
        if request.POST['logout'] == 'logout':
            logout(request)
            i = 0
            return redirect("index")

    except:
        pass

    if request.method == "POST" and form.is_valid and i != 0:
        form.save()
        user = authenticate(request, username=form.data.get("username"), password=form.data.get("password2"))
        login(request, user)
        return redirect("index")

    return render(request, 'auth.html', {"form": form})


def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    login = AuthenticationForm()
    if request.method == "POST":
        bound_form = RestourantForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        return render(request, "index.html", {'restorants': restorants,
                                          'form': bound_form})


    form = RestourantForm()
    return render(request, 'index.html', {'restorants': restorants,
                                          'form': form,
                                          "login": login})


def rest_detail(request, rest_detail):
    name = get_object_or_404(Restorant, id=rest_detail)
    return render(request, "rest_detail.html", {"name": name})
