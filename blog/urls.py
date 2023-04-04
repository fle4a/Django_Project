from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),path('employees/', views.employee_list, name='blog-employee-list'),path('result/', views.execute_query, name='blog-result'),path('request/', views.execute_query, name='blog-request'),path('analyze/', views.analyze, name='blog-analyze'),
    path('result/', views.analyze, name='blog-result'),  path('register/', views.register, name='blog-register'),path('login/', views._login, name='blog-login'),path('examples/', views.examples, name='blog-examples'),path('create_person/', views.create_person, name='blog-create-person'),
]
