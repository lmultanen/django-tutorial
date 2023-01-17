from django.urls import path
from firstapp import views

urlpatterns = [
    path("date/", views.current_time),
    path("helloworld/", views.hello_world)
]