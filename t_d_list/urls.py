from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    tag_complete
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tags_list"
    ),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tags_create"
    ),
    path(
        "tags/update/<int:pk>/",
        TagsUpdateView.as_view(),
        name="tags_update"
    ),
    path(
        "tags/delete/<int:pk>/",
        TagsDeleteView.as_view(),
        name="tags_delete"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_create"
    ),
    path(
        "task/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task_update"
    ),
    path(
        "task/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task_delete"
    ),
    path(
        "task/<int:pk>/is_done",
        tag_complete,
        name="tag-complete"
    ),
]

app_name = "t_d_list"
