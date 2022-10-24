from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView,DeleteView
from .models import SpLic
from .forms import SpLicForm, SpLicForm2
from .filter import SnippetFilter

class SpLic_view(ListView):
    model = SpLic
    template_name = 'sp/LicView_view.html'
    queryset =SpLic.objects.all().filter(deleted='False')


class SpLicDeleteLicView(UpdateView):
    model = SpLic
    template_name = 'sp/delete.html'
    success_url = '/sp/'
    #form_class = SpLicForm
    fields = ['deleted']


class SpLicUpdateView(UpdateView):
    model = SpLic
    template_name = 'sp/detail_app_view.html'
    form_class = SpLicForm2
    success_url = '/sp/'


def SPcreate(request):
    error = ''
    if request.method =='POST':
        form = SpLicForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sp/')#Перенос
        else:
            error='Форма заполнения неверная'
    form = SpLicForm2()
    data={
        'form':form,
        'error':error
    }
    return render(request,'sp/create_app.html',data)

class SnippetListView(ListView):
    model = SpLic
    template_name = 'sp/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context

