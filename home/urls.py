from django.urls import path
from .views import home, my_logout
from django.views.generic import TemplateView
from .views import HomeView, SimpleView, MethodsView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name = 'tamplate_view'),
    path('home3/', HomeView.as_view(), name = 'custom_tamplate_view'),
    path('view/', SimpleView.as_view(), name = 'simple_view'),
    path('method/', MethodsView.as_view(), name = 'method'),
]