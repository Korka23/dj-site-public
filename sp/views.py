from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from .models import SpLic
from .forms import SpLicForm

class SpLic_view(ListView):
    model = SpLic
    template_name = 'sp/LicView_view.html'
    queryset =SpLic.objects.all()


class SpLicDeleteLicView(UpdateView):
    model = SpLic
    template_name = 'sp/delete.html'
    success_url = '/sp/'
    #form_class = SpLicForm
    fields = ['deleted']


class SpLicUpdateView(UpdateView):
    model = SpLic
    template_name = 'sp/detail_app_view.html'
    form_class = SpLicForm
    success_url = '/sp/'


def SPcreate(request):
    error = ''
    if request.method =='POST':
        form = SpLicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sp/')#Перенос
        else:
            error='Форма заполнения неверная'
    form = SpLicForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'sp/create_app.html',data)


# Create your views here.
