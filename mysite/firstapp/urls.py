from django.urls import path
from firstapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("date/", views.current_time, name='time'),
    path("helloworld/", views.hello_world, name='hello-world')
]