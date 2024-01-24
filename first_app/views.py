from django.shortcuts import render,redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_task(request):
    if request.method == 'POST': 
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_tasks')
    else:
        task = TaskForm()
    return render(request,'add_task.html',{'form':task})

def show_tasks(request):
    data = TaskModel.objects.all()
    print(data)
    return render(request,'show_tasks.html',{'task':data})

def edit_task(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance=task)
    if request.method == 'POST': 
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('show_tasks')

def complete_task(request,id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect('completed_task')

def completed_task(request):
    completed_task = TaskModel.objects.filter(is_completed = True)
    return render(request,'completed_task.html',{'completed_task':completed_task})
