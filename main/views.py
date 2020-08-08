from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
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
    fields = '__all__'

class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    fields = '__all__'
    context_object_name = 'colleges'  

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'college_create.html'
    fields = "__all__"
    success_url = '/college'

class StudentCreate(CreateView):
    model = models.Student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/college'

class UpdateCollege(UpdateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'

class StudentList(ListView):
    model = models.Student
    model2 = models.College
    template_name = 'student_list.html'
    fields = '__all__'
    context_object_name = 'students'

class StudentDelete(DeleteView)
    


