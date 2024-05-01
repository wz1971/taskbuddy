from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserEditForm, TaskSearchForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Project, Task, Subtask
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home_view(request):
    return render(request, "projects/home.html")

def about_view(request):
    return render(request, "projects/about.html")

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/cbv/project_list.html"
    context_object_name = "project_list"
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/cbv/project_form.html"
    fields = ["title", "deadline", "user"]
    success_url = reverse_lazy("project-list")

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/cbv/project_detail.html"
    context_object_name = "project"

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "projects/cbv/project_form.html"
    fields = ["title", "deadline", "user"]
    context_object_name = "project"
    success_url = reverse_lazy("project-list")

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/cbv/project_confirm_delete.html"
    success_url = reverse_lazy("project-list")
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "projects/cbv/task_list.html"
    context_object_name = "task_list"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "projects/cbv/task_form.html"
    fields = ["title", "description", "priority", "status", "deadline", "project", "user"]
    success_url = reverse_lazy("task-list")

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "projects/cbv/task_detail.html"
    context_object_name = "task"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "projects/cbv/task_form.html"
    fields = ["title", "description", "priority", "status", "deadline", "project", "user"]
    context_object_name = "task"
    success_url = reverse_lazy("task-list")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "projects/cbv/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")

class SubtaskListView(LoginRequiredMixin, ListView):
    model = Subtask
    template_name = "projects/cbv/subtask_list.html"
    context_object_name = "subtask_list"

class SubtaskCreateView(LoginRequiredMixin, CreateView):
    model = Subtask
    template_name = "projects/cbv/subtask_form.html"
    fields = ["title", "description", "status", "task", "user"]
    success_url = reverse_lazy("subtask-list")

class SubtaskDetailView(LoginRequiredMixin, DetailView):
    model = Subtask
    template_name = "projects/cbv/subtask_detail.html"
    context_object_name = "subtask"

class SubtaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Subtask
    template_name = "projects/cbv/subtask_form.html"
    fields = ["title", "description", "status", "task", "user"]
    context_object_name = "subtask"
    success_url = reverse_lazy("subtask-list")

class SubtaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Subtask
    template_name = "projects/cbv/subtask_confirm_delete.html"
    success_url = reverse_lazy("subtask-list")
    
def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")
    return render(request, "projects/login.html", {"login_data": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'projects/cbv/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def task_search_view(request):
    if request.method == "GET":
        form = TaskSearchForm()
        return render(
            request, "projects/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        form = TaskSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            status = form.cleaned_data["status"]
            priority = form.cleaned_data["priority"]

            found_tasks = Task.objects.filter(title__icontains=title)

            if status:
                found_tasks = found_tasks.filter(status=status)

            if priority:
                found_tasks = found_tasks.filter(priority=priority)

            context = {"task_list": found_tasks}
            return render(request, "projects/cbv/task_list.html", context)
        else:
            return render(
                request, "projects/form_search.html", context={"search_form": form}
            )
