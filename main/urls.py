from django.urls import path
from main import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name = 'college'),
    path('college/' , views.CollegeList.as_view()),
    path('college_create/' , views.CollegeCreate.as_view()),
    path('update_college/<int:pk>' , views.UpdateCollege.as_view()),
    path('student_create/' , views.StudentCreate.as_view()),
    path('student_list/' , views.StudentList.as_view()),
    path('student_delete/<int:pk>' , views.StudentDelete.as_view())
]