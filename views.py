from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
class Companylistview(ListView):
    model=Company
    template_name = "company_list.html"


class CompaneyDetailView(DetailView):
    model=Company
    template_name = "company_detail.html"

class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
    template_name = "company_form.html"
    success_url = "/list/"



class CompanyUpdateView(UpdateView):
    model=Company
    fields=('location','ceo','name')
    template_name = "company_form.html"
    success_url = "/list/"



from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = "/list/"
    template_name = 'company_confirm_delete.html'
# Create your views here.
