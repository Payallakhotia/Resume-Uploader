from django.urls import path
from api import views

urlpatterns=[
    path('', views.home, name = "home"),
    path('resume/',views.ResumeView.as_view,name='resume'),
    path('list/',views.ResumeView.as_view,name='list'),
]