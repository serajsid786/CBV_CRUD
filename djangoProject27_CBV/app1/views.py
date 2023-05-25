from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HelloView(View):
    def get(self,request):
        s1='<h1>This output is genrated by class based views</h1>'
        return HttpResponse(s1)
