from django.urls import path
from main import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name = 'college'),
    path('college/' , views.CollegeList.as_view())
]