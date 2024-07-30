from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_tasks, name="get_all_tasks"),
    path("<int:pk>", views.get_task, name="get_individual_task"),
    path("create/", views.create_todotask, name="create-todo"),
    path("<int:pk>/update", views.update_todotask, name="update_task"),
    path("<int:pk>/delete", views.delete_task, name="delete_task"),
]
