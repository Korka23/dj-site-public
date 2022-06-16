from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from .models import SzpLic
from .forms import SzpLicForm

class SZPLic_view(ListView):
    model = SzpLic
    template_name = 'szp/LicView_view.html'
    queryset = SzpLic.objects.all()


class SZPDeleteLicView(UpdateView):
    model = SzpLic
    template_name = 'szp/delete.html'
    success_url = '/szp/'
    fields = ['deleted']


class SZPLicUpdateView(UpdateView):
    model = SzpLic
    template_name = 'szp/detail_app_view.html'
    form_class = SzpLicForm
    success_url = '/szp/'


def SZPcreate(request):
    error = ''
    if request.method =='POST':
        form = SzpLicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/szp/')#Перенос
        else:
            error='Форма заполнения неверная'
    form=SzpLicForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'szp/create_app.html',data)


# Create your views here.
