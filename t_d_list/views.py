from django.views import generic
from django.shortcuts import render

from t_d_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"


class TagsListView(generic.ListView):
    model = Tag
    template_name = 'tags_list.html'
    context_object_name = "tags"
