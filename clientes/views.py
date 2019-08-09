from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

class PersonView(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        get_vars = super().get_context_data(**kwargs)
        get_vars['now'] = timezone.now()
        return get_vars

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'

class PersonUpdate(UpdateView):
    model = Person
    template_name = 'clientes/person_update_form.html'    
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_view')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_view')

    def get_success_url(self):
        return reverse_lazy('person_list_view')