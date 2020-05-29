from django.shortcuts import render,HttpResponse
from rest.apps.main.models import Restorant

# Create your views here.
def index(request):
    restorants = Restorant.objects.all().order_by("-rating_restorant")
    return render(request,'index.html', {'restorants': restorants})

def rest_detail(request,rest_detail):
    name = Restorant.objects.get(id=rest_detail)
    print(name)
    return render(request,"rest_detail.html", {"name":name})

def form(request):
    s = request.POST.dict()
    data = Restorant(name_restorant = s.get("name_restorant"),
                     rescription_restorant = s.get("rescription_restorant"),
                     rating_restorant= int(s.get("rating_restorant")))
    data.save()

    return HttpResponse(s.get("name_restorant"))
