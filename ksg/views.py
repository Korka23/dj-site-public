from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from django.http import HttpResponse
from .models import dj_ksg_p, LicDop, LicMash
from rest_framework import viewsets
from .forms import KSGForms, LicDopForm, LicMashForm
#from .serializers import HeroSerializer



class KSGView(ListView):
    model = dj_ksg_p
    template_name = 'ksg/kss.html'
    queryset = dj_ksg_p.objects.all()


class NewDataView(DetailView):
    model = dj_ksg_p
    template_name = 'ksg/create.html'
    context_object_name = 'dj_ksg_p'


class DeleteKSG(DeleteView):
    model = dj_ksg_p
    template_name = 'ksg/delete.html'
    success_url = '/ksg/'


class NewUpdateView(UpdateView):
    model=dj_ksg_p
    template_name = 'ksg/detail_view.html'
    #fields = ['name','c_prof','smj_prof','KSG']
    form_class = KSGForms
    success_url = '/ksg/'


class LicView_view(ListView):
    model = LicMash
    template_name = 'ksg/LicView_view.html'
    queryset =  LicMash.objects.all()

class CreateLicView(DetailView):
    model = LicMash
    template_name = 'ksg/create_lic.html'
    context_object_name = 'LicMash'


class DeleteLicView(DeleteView):
    model = LicMash
    template_name = 'ksg/delete.html'
    success_url = '/LicView/'


class LicUpdateView(UpdateView):
    model = LicMash
    template_name = 'ksg/detail_lic_view.html'
    #fields = ['name','c_prof','smj_prof','KSG']
    form_class = LicMashForm
    success_url = '/LicView/'


def index(request):
    return render(request, 'ksg/layout.html')


def create(request):
    error = ''
    if request.method =='POST':
        form= KSGForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ksg/')#Перенос
        else:
            error='Форма заполнения неверная'
    form=KSGForms()
    data={
        'form':form,
        'error':error
    }
    return render(request,'ksg/create.html',data)

def CreateLic(request):
    error = ''
    if request.method =='POST':
        form = LicMashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/LicView/')#Перенос
        else:
            error='Форма заполнения неверная'
    form=LicMashForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'ksg/create_lic.html', data)
