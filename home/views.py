from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.generic import TemplateView, View


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

class HomeView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Variavel_Injetada'] = "Veriavel injetada no contexto da View"
        return context

class SimpleView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("View simples")

class MethodsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'methods.html', {'method':'get'})

    def post(self, request, *args, **kwargs):
        return render(request, 'methods.html', {'method':'post'})
