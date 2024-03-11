from django.views import generic
from t_d_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "t_d_list/task_list.html"
    context_object_name = "tasks"


class TagsListView(generic.ListView):
    model = Tag
    template_name = 't_d_list/tags_list.html'
    context_object_name = "tags"
