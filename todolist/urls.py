from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    # path("", views.post_list, name='list'),
    # path("new-post/", views.new_post, name='new_post'),
    # path("<slug:post_slug>", views.post_page, name='page')
    path("", views.list_todo),
    path("add-task/", views.add_task, name='add_task'),
    # path("delete-task/<int:task_id>/", views.delete_task, name='delete_task'),
]
