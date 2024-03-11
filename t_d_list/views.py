from django.views import generic

from t_d_list.forms import TaskForm
from t_d_list.models import Task, Tag
from django.urls import reverse_lazy


class TaskListView(generic.ListView):
    model = Task
    template_name = "t_d_list/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("t_d_list:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("t_d_list:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("t_d_list:task_list")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "t_d_list/tags_list.html"
    context_object_name = "tags"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("t_d_list:tags_list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("t_d_list:tags_list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("t_d_list:tags_list")
