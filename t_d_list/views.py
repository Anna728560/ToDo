from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from t_d_list.forms import TaskForm
from t_d_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "t_d_list/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").all()


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    success_url = reverse_lazy("t_d_list:task_list")


class TaskUpdateView(generic.UpdateView):
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
    success_url = reverse_lazy("t_d_list:tags_list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("t_d_list:tags_list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("t_d_list:tags_list")


def tag_complete(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("t_d_list:task_list"))
