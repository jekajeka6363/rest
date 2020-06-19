from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth, name="auth"),
    path('login', views.log, name="login"),
    path('<int:rest_detail>', views.rest_detail, name="rest-detail"),
    path('create', views.index, name="rest-create"),

]
