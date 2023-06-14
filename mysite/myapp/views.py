from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('task_list')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('login')



@login_required
def task_list(request):
    Tasks=Task.objects.filter(user=request.user)
    return render(request,"task_list.html",{"tasks":Tasks})

@login_required
def task_create(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_update(request,id):
    task=get_object_or_404(Task,pk=id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form=TaskForm(instance=task)
    return render(request,"task_form.html",{"form":form})

@login_required
def task_delete(request,id):
    task=get_object_or_404(Task,pk=id)
    task.delete()
    return redirect("task_list")