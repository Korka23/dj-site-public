from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from .models import Szp1Lic
from .forms import Szp1LicForm

class SZP1Lic_view(ListView):
    model = Szp1Lic
    template_name = 'szp1/LicView_view.html'
    queryset =  Szp1Lic.objects.all()


class SZP1DeleteLicView(UpdateView):
    model = Szp1Lic
    template_name = 'szp1/delete.html'
    success_url = '/szp1/'
    fields = ['deleted']


class SZP1LicUpdateView(UpdateView):
    model = Szp1Lic
    template_name = 'szp1/detail_app_view.html'
    form_class = Szp1LicForm
    success_url = '/szp1/'


def SZP1create(request):
    error = ''
    if request.method =='POST':
        form= Szp1LicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/szp1/')#Перенос
        else:
            error='Форма заполнения неверная'
    form=Szp1LicForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'szp1/create_app.html',data)


# Create your views here.
