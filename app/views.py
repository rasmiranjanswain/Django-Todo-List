from django.shortcuts import render,redirect
from app.models import Todo

# Create your views here.

def index(request):
    alltask = Todo.objects.all()
    context = { 'tasks' : alltask}
    if request.method == "POST":
        todo = request.POST.get('todo')
        desc = request.POST.get('description')
        data = Todo(todo=todo,desc=desc)
        data.save()
    return render(request,'index.html',context)

def deletetask(request,pk):
    task = Todo.objects.get(pk=pk)
    task.delete()
    return redirect('index')

