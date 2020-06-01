from django.shortcuts import render, HttpResponse, redirect
from rest.apps.main.models import Restorant
from .forms import NameForm
# Create your views here.


def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    if request.method == "POST" :
        bound_form = NameForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return render(request, "index.html", {'restorants': restorants,
                                          'form': bound_form})
        elif bound_form.errors.__len__() > 0:
            return render(request, "index.html", {'restorants': restorants,
                                                  'form': bound_form})

    form = NameForm()
    return render(request, 'index.html', {'restorants': restorants,
                                          'form': form})


def rest_detail(request, rest_detail):
    name = Restorant.objects.get(id=rest_detail)
    return render(request, "rest_detail.html", {"name": name})
