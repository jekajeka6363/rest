from django.shortcuts import render,HttpResponse
from rest.apps.main.models import Restorant

# Create your views here.
def index(request):
    list = Restorant.objects.all()
    return render(request,'index.html', {'list': list,})