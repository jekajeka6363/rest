from django.shortcuts import render,HttpResponse
from rest.apps.main.models import Restorant

# Create your views here.
def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    return render(request,'index.html', {'restorants': restorants})
