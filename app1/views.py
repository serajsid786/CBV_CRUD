from django.shortcuts import render
from .models import Employee
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee_form.html'
    success_url = '/'

class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeDetails(DetailView):
    model = Employee
    template_name = 'employee_details.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee_form.html'
    success_url = '/list'

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = '/list'