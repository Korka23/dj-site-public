from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.http import HttpResponse
from app.models import LicAppNew
from app.forms import LicAppNewForm, PersonCreationForm, djFormAp, LicAppNewForm2
from .filter import SnippetFilter


class LicAppNew_view(ListView):
    model = LicAppNew
    template_name = 'app/LicView_view.html'
    #template_name = 'app/test_view.html'
    queryset = LicAppNew.objects.all().filter(deleted='False')
    '''
    def display_lic(self):
       b = LicAppNew.get_c_serv_display()
       HttpResponse(b)
'''
    '''
    def get_c_serv_display(self):
        model = LicAppNew
        form =LicAppNewForm
        error = ''
        data = {
            'form': form,
            'error': error,
            'model': model
                 }
        return render(request, 'app/create_app.html', data)
'''

class CreateLicAppNew(DetailView):
    model = LicAppNew
    template_name = 'app/create_app.html'
    context_object_name = 'App'


class AppDeleteLicView(UpdateView):
    model = LicAppNew
    template_name = 'app/delete.html'
    #form_class = LicAppNewForm
    success_url = '/app/'
    fields = ['deleted']


class AppLicUpdateView(UpdateView):
    model = LicAppNew
    template_name = 'app/detail_app_view.html'
    form_class = LicAppNewForm2
    success_url = '/app/'


def Appcreate(request):
    error = ''
    if request.method =='POST':
        form = LicAppNewForm2(request.POST)
        if form.is_valid() and form.instance.get_fc_mo_display() == form.instance.name:
            form.save()
            return redirect('/app/')#Перенос
        else:
            error='Форма заполнения неверная'
    form = LicAppNewForm2()
    data = {
        'form': form,
        'error': error,
    }
    return render(request,'app/create_app.html',data)


def Appcreate_list(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'app/home.html', {'form': form})


def AppLicUpdateView_list(request, pk):
    person = get_object_or_404(LicAppNew, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'app/home.html', {'form': form})


def load_cities(request):
    id = request.GET.get('id_prof')
    fc_mo = LicAppNew.objects.filter(id=id).all()
    return render(request, 'app/city_dropdown_list_options.html', {'fc_mo': fc_mo})#maybe id
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

class AppCreateTest(CreateView):
    model = LicAppNew
    form_class = LicAppNewForm
    template_name = 'app/create_app.html'
    success_url = '/app/'

def indus(request):
    result = LicAppNew.objects.all()
    return render(request, 'app/indus.html', {"LicAppNew": result})


def BootstrapFilterView(request):
    qs = LicAppNew.objects.all()
    context = {
        'queryset': qs
    }
    return render(request, "app/bootstrap_form.html", context)

class SnippetListView(ListView):
    model = LicAppNew
    template_name = 'app/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context



