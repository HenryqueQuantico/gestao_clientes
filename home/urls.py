from django.urls import path
from .views import home, my_logout
#from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
]