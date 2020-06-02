from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from rest.apps.main.models import Restorant
from .forms import RestourantForm

def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    if request.method == "POST" :
        bound_form = RestourantForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        return render(request, "index.html", {'restorants': restorants,
                                          'form': bound_form})


    form = RestourantForm()
    return render(request, 'index.html', {'restorants': restorants,
                                          'form': form})


def rest_detail(request, rest_detail):
    name = get_object_or_404(Restorant, id=rest_detail)
    return render(request, "rest_detail.html", {"name": name})
