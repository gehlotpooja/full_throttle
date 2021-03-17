from django.urls import path
from . import views
urlpatterns = [
    path(r'save_org/', views.save_org_api),
    path(r'register/', views.register_api),
    path(r'login/', views.login),
    path(r'add_task/', views.add_task_api),
    path(r'get_task/', views.get_task_api),
    path(r'delete/', views.delete),
]
