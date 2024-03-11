from django.urls import path
from .views import TagsListView, TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagsListView.as_view(), name="tags_list")
]

app_name = "t_d_list"
