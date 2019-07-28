from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView


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

