from django.urls import path
from .views import (
    TagsListView,
    TaskListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagsListView.as_view(), name="tags_list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags_create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags_update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags_delete"),
]

app_name = "t_d_list"
