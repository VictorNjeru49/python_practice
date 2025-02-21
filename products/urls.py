from django.urls import path
from . import views

# views = views.index
urlpatterns = [
    path('',views.index),
    path('new', views.new),
]