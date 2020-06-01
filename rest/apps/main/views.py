from django.shortcuts import render,HttpResponse
from rest.apps.main.models import Restorant
from .forms import NameForm
# Create your views here.


def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    form = NameForm()
    return render(request, 'index.html', {'restorants': restorants,
                                          'form': form})


def rest_detail(request, rest_detail):
    name = Restorant.objects.get(id=rest_detail)
    return render(request, "rest_detail.html", {"name": name})


def form(request):
    return render(request, 'form.html')
