from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from django.http import HttpResponse
from .models import dj_ksg_p
from rest_framework import viewsets
from .forms import KSGForms
#from .serializers import HeroSerializer



class KSGView(ListView):
    model = dj_ksg_p
    template_name = 'ksg/kss.html'
    queryset = dj_ksg_p.objects.all()


class NewDataView(DetailView):
    model = dj_ksg_p
    template_name = 'ksg/create.html'
    context_object_name = 'dj_ksg_p'


class DeleteKSG(UpdateView):
    model = dj_ksg_p
    template_name = 'ksg/delete.html'
    success_url = '/ksg/'
    fields = ['deleted']

class NewUpdateView(UpdateView):
    model=dj_ksg_p
    template_name = 'ksg/detail_view.html'
    form_class = KSGForms
    success_url = '/ksg/'


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

