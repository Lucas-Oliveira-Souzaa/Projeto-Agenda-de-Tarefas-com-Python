from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            return render(
                request,
                "tarefas/login.html",
                {
                    "error": "Usuário ou senha inválidos."
                }
            )

    return render(request, "tarefas/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def home(request):

    tasks = Task.objects.all()

    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:

        if task.done:
            completed_tasks += 1

    remaining_tasks = total_tasks - completed_tasks

    pct = 0

    if total_tasks > 0:
        pct = (completed_tasks / total_tasks) * 100

    return render(
        request,
        "tarefas/home.html",
        {
            "tasks": tasks,
            "total": total_tasks,
            "completed": completed_tasks,
            "remaining": remaining_tasks,
            "pct": pct
        }
    )


@login_required
def add(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

    return redirect("home")


@login_required
def toggle(request, id):

    task = get_object_or_404(Task, id=id)

    task.done = not task.done

    task.save()

    return redirect("home")


@login_required
def delete(request, id):

    task = get_object_or_404(Task, id=id)

    task.delete()

    return redirect("home")