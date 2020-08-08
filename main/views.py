from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    DetailView,
    ListView
)

from main import models
# Create your views here.

class Index(View):
    def get(self,request):
        return HttpResponse("GET request")

    def post(self,request):
        return HttpResponse("POST request")


'''
Django provides us with 5 generic views:
1) Detail View
2)List View
3)Create View
4)Update View
5)Delete View
'''

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name = 'colleges'    


