from django.urls import path
from mysite import views

urlpatterns = [
    path("",views.home,name = "home")
]
