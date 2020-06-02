from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:rest_detail>', views.rest_detail, name="rest-detail"),
    path('create', views.index, name="rest-create")

]
