from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from app.models import LicAppNew
from app.forms import LicAppNewForm

class LicAppNew_view(ListView):
    model = LicAppNew
    template_name = 'app/LicView_view.html'
    queryset =  LicAppNew.objects.all()

class CreateLicAppNew(DetailView):
    model = LicAppNew
    template_name = 'app/create_app.html'
    context_object_name = 'App'


class AppDeleteLicView(UpdateView):
    model = LicAppNew
    template_name = 'app/delete.html'
    form_class = LicAppNewForm
    success_url = '/app/'


class AppLicUpdateView(UpdateView):
    model = LicAppNew
    template_name = 'app/detail_app_view.html'
    form_class = LicAppNewForm
    success_url = '/app/'


def Appcreate(request):
    error = ''
    if request.method =='POST':
        form= LicAppNewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/')#Перенос
        else:
            error='Форма заполнения неверная'
    form=LicAppNewForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'app/create_app.html',data)


# Create your views here.
