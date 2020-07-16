from django.urls import path, re_path, include
app_name = 'api'
from . import views

urlpatterns = [
    re_path(r'^tasks/', views.tasks, name='tasks')
]
